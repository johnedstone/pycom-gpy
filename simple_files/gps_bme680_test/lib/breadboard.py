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
    Configuration #1
    ================
    Pytracker v2 connected to GPy by I2C bus on breadboard
    Pytracker v2 powered by USB
    bme680 connected to GPy by SPI
    ----------------------------------------
    *tReset -- gReset (optional: appears to work either way)
    *tP0 --- gP0 UART_RX
    *tP1 --- gP1 UART_TX

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
    
    Does this configuration work with b9e29b3:projects/post_json_data/main.py? Yes

    Added back pins tP13-15 to gP13-15 as if stacked, as recommended,
    appear to work with this script and b9e29b3:projects/post_json_data/main.py

    And, then, adding back tP8-12 to gP8-12, as if stacked as recommended,
    appear to work with this script and b9e29b3:projects/post_json_data/main.py

    And then, lastly, adding back tP2 to gP2, as if stacked, as recommended,
    appear to work with this script and b9e29b3:projects/post_json_data/main.py

    Configuration #2: this pinout runs as above That is, successful with breadboard run from REPL as
    ================
        import breadboard
        breadboard.repl_test()
    And, runs with the current main.py succesfully
    Pytracker v2 connected to GPy by I2C bus on breadboard
    Pytracker v2 powered by USB
    bme680 connected to GPy by SPI
    Using all of the recommened cabling as described in the Pytrack v2 documentaion
    ----------------------------------------
    PyTracker --- GPy on J5 module pins 1, 2(P0), 3, 4, 6, 10, 11. 12, 13, 14(P12)
    PyTracker --- GPy on J6 module pins 1(VIN), 2, 3, 4, 5, 6, 12, 13, 14(P13)

    bme680 on breadboard connected to GPY by SPI on breadboard
    [reference for pinout](https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/python-circuitpython-test)
    ------------------------------
    bVIN --- gVIN (3.5-5.5V) (module pin 28)
    bGND --- gGND (module pin 27)
    bSCK --- gP20
    bSDO --- gP18 (MISO)
    bSDI --- gP19 (MOSI)
    bCS  --- gP3 (module pin 5)

"""
from machine import I2C, SPI, Pin

from pycoproc_2 import Pycoproc
from L76GNSS import L76GNSS
from bme680 import BME680_SPI

def repl_test():
    return_list = []

    # GPS I2C
    i2c0 = I2C(0, mode=I2C.MASTER, pins=('P22', 'P21'))
    py0 = Pycoproc(i2c=i2c0, sda='P22', scl='P21')
    return_list.append('GPY read product id: {}'.format(py0.read_product_id()))
    return_list.append('GPY docs product id: {}'.format(Pycoproc.USB_PID_PYTRACK))
    l76 = L76GNSS(py0, timeout=30, buffer=512)
    return_list.append('GPS coordinates: {}'.format(l76.coordinates()))


    ######  bme680 SPI  ######################

    # Configuration #1
    # this uses the SPI not default pins for CLK, MOSI and MISO ('P4', 'P20' and ``P19``)
    #spi = SPI(0, mode=SPI.MASTER, baudrate=2000000, polarity=0, phase=0, pins=('P4','P20','P19'))

    # Configuration #2
    # this uses the SPI not default pins for CLK, MOSI and MISO ('P20', 'P19' and ``P18``)
    spi = SPI(0, mode=SPI.MASTER, baudrate=2000000, polarity=0, phase=0, pins=('P20','P19','P18'))

    cs = Pin('P3', Pin.OUT, value=1) # same for both configurations

    bme = BME680_SPI(spi, cs)
    bme.sea_level_pressure = 1013.25
    temperature_offset = -5

    return_list.append('bme.temp: {}'.format(bme.temperature))
    return_list.append('bme.humidity: {}'.format(bme.humidity))
    return_list.append('bme.pressure: {}'.format(bme.pressure))
    return_list.append('bme.gas: {}'.format(bme.gas))
    return_list.append('bme.altitude: {}'.format(bme.altitude))

    return return_list

# vim: ai et ts=4 sw=4 sts=4 nu
