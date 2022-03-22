"""
https://github.com/robert-hh/BME680-Micropython
using P8 and 10, since Pytrack v2 uses P9
https://docs.pycom.io/firmwareapi/pycom/machine/i2c/
"""

from machine import I2C

i2c = I2C(1, pins=('P19','P20')) # module pin #5 and #6
i2c.init(I2C.MASTER, baudrate=20000) # init as a master
print(i2c)
i2c.scan()
i2c.deinit()
