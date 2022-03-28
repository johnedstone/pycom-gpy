from machine import SPI, Pin
from bme680 import BME680_SPI

def get_bme680_data():
    bme680_data = {
        'temperature': None,
        'humidity': None,
        'pressure': None,
        'gas': None,
        'altitude': None,
        }

    spi = SPI(0, mode=SPI.MASTER, baudrate=2000000, polarity=0, phase=0, pins=('P4','P20','P19'))
    cs = Pin('P3', Pin.OUT, value=1)
    bme = BME680_SPI(spi, cs)

    bme.sea_level_pressure = 1013.25
    temperature_offset = -5

    bme680_data['temperature'] = '{}'.format(bme.temperature)
    bme680_data['humidity'] = '{}'.format(bme.humidity)
    bme680_data['pressure'] = '{}'.format(bme.pressure)
    bme680_data['gas'] = '{}'.format(bme.gas)
    bme680_data['altitude'] = '{}'.format(bme.altitude)

    return bme680_data

# vim: ai et ts=4 sts=4 sw=4 nu
