"""
Purpose: connecting GPy, Pytrack v2 (powered by USB), Pysense v2
         from Pycom.io, and bme680 from Adafruit using a breadboard

Ref:
    [for the Adafruit bme680 library](https://github.com/robert-hh/BME680-Micropython)
    [for Pycom documentation](https://docs.pycom.io/)
    [for Pycom source code](https://github.com/pycom/pycom-libraries/)

Key:
    tP0 = P0 pin on the Pytracker v2,
        which is module pin 2 (J5) UART_RX per documentation -
        https://docs.pycom.io/gitbook/assets/PyTrack2X_specsheet.pdf

    gP0 = P0 pin on GPy,
        which is module pin 2 - https://docs.pycom.io/gitbook/assets/specsheets/Pycom_002_Specsheets_GPy_v2.pdf

    bVIN = bme680 VIN pin, bme680 is from Adafruit - 
        https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/python-circuitpython

    sP0 = P0 pin on Pysense v2,
        which is module pin 2 (J5) UART_RX per documentation - https://docs.pycom.io/gitbook/assets/PySense2X_specsheet.pdf

    * means these pins would line up, if the two were stacked

Connection:
    Pytracker v2 connected to GPy by I2C bus on breadboard
    ----------------------------------------
    *tReset --- gReset
    *tP0 --- gP0 UART_RX
    *tP1 --- gP1 UART_TX
    *tP2 --- gP2 (per PyTracker documentation)

    *tP9 --- gP9 (per PyTracker documentation)
    *tP10 --- gP10 (per PyTracker documentation)
    *tP11 --- gP11 (per PyTracker documentation)
    *t(not marked as P) (module j5 pin 14)  --- gP12 (per PyTracker documentation)

    *t5V (VCC module J6 pin 1) --- gVIN (3.5-5.5V) (module pin 28)
    *tGND (GND module J6 pin 2) -- gGND (module pin 27)
    *t3V3 (3V3_MOD module J6 pin 3) --- g3.3V out (module pin 26)
    *tP22 (SDA module pin J6 5) SDA --- gP22 
    *tP21 (SCL module pin J6 6) SCl --- gP21


    bme680 on breadboard connected to GPY by SPI on breadboard
    [reference for pinout](https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/python-circuitpython-test)
    ------------------------------
    bVIN --- gVIN (3.5-5.5V) (module pin 28)
    bGND --- gGND (module pin 27)
    bSCK --- gP4 
    bSDO --- gP19 (MISO)
    bSDI --- gP20 (MOSI)
    bCS  --- gP3

"""
from machine import SPI, Pin
from bme680 import BME680_SPI

# bme680 SPI
# this uses the SPI not default pins for CLK, MOSI and MISO ('P4', 'P20' and ``P19``)
spi = SPI(0, mode=SPI.MASTER, baudrate=2000000, polarity=0, phase=0, pins=('P4','P20','P19'))
cs = Pin('P3', Pin.OUT, value=1)
bme = BME680_SPI(spi, cs)
bme.sea_level_pressure = 1013.25
temperature_offset = -5

def get_bme680_data():

    bme_data = {
        'temperature': None,
        'humidity': None,
        'pressure': None,
        'gas': None,
        'altitude': None,
    }
    return bme_data

    bme_data['temperature'] = '{}'.format(bme.temperature)
    bme_data['humidity'] = '{}'.format(bme.humidity)
    bme_data['pressure'] = '{}'.format(bme.pressure)
    bme_data['gas'] = '{}'.format(bme.gas)
    bme_data['altitude'] = '{}'.format(bme.altitude)

    return bme_data

# vim: ai et ts=4 sw=4 sts=4 nu
