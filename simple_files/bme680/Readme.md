#### Notes
* using the bme680 library [link](https://github.com/robert-hh/BME680-Micropython)
* using bme680  board from Adafruit [link](https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/arduino-wiring-test)
* using GPy from Pycom
* using Pytracker v2 from Pycom
* Pinned out Pytracker per documentation [link, section 5.2 "Module (WiPy, GPy or LoPy) socket pinout", page 07, except for the 3 `SD_` pins](https://docs.pycom.io/gitbook/assets/PyTrack2X_specsheet.pdf)
* Added bme680 to P20 (sda) and P19 (sdc)
* [pressure to altitude](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas.pdf)

```
>>> from machine import I2C
>>> i2c = I2C(2, pins=('P20', 'P19'))
>>> i2c.scan()
[119]
>>> os.listdir('lib')
['L76GNSS.py', 'LIS2HH12.py', 'LTR329ALS01.py', 'MPL3115A2.py', 'SI7006A20.py', 'bme680.py', 'helper_functions.py', 'private_vars.py', 'pycom_bme680.py', 'pycoproc_1.py', 'pycoproc_2.py']
>>> # added two libraries ...
>>> import pycom_bme680
>>> import bme680
>>> dir(bme680)
['__class__', '__name__', 'const', '__file__', 'hex', 'math', 'struct', 'time', '_BME680_SAMPLERATES', '_BME680_FILTERSIZES', '_LOOKUP_TABLE_1', '_LOOKUP_TABLE_2', '_read24', 'Adafruit_BME680', 'BME680_I2C', '_POLL_PERIOD_MS', '_MODE_MSK', '_MODE_POS', 'BME680_SPI']
>>> dir(pycom_bme680)
['__class__', '__name__', 'const', '__file__', 'hex', 'math', 'struct', 'time', '_BME680_SAMPLERATES', '_BME680_FILTERSIZES', '_LOOKUP_TABLE_1', '_LOOKUP_TABLE_2', '_read24', 'Adafruit_BME680', 'BME680_I2C']
>>> bme = bme680.BME680_I2C(i2c)
>>> bme.humidity
41.47574
>>> bme.temperature
21.65793
>>> bme.pressure
971.7263
>>> bme.gas
1130
>>> bme.sea_level_pressure = 1013.25
>>> temperature_offset = -5
>>> bme.altitude
351.6285

```
