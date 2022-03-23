from machine import I2C

from pycoproc_2 import Pycoproc
from L76GNSS import L76GNSS
import bme680

def repl_test():
    return_list = []
    return_list.append("This is with minimal pins, e.g. reset, power, sda, scl")
    i2c0 = I2C(0, mode=I2C.MASTER, pins=('P22', 'P21'))
    py0 = Pycoproc(i2c=i2c0, sda='P22', scl='P21')
    return_list.append(py0.read_product_id())
    return_list.append(Pycoproc.USB_PID_PYTRACK)

    l76 = L76GNSS(py0, timeout=30, buffer=512)
    return_list.append(l76.coordinates())

    #i2c1 = I2C(1, pins=('P20', 'P19')) #works
    i2c1 = I2C(1, mode=I2C.MASTER,pins=('P20', 'P19')) #works
    bme = bme680.BME680_I2C(i2c1) #works
    #py1 = Pycoproc(i2c=i2c1, sda='P20', scl='P19') # did not work
    #bme = bme680.BME680_I2C(py1) # did not work
    
    return_list.append(bme.humidity)
    return_list.append(bme.temperature)
    return_list.append(bme.pressure)
    return_list.append(bme.gas)
    bme.sea_level_pressure = 1013.25
    temperature_offset = -5
    return_list.append(bme.altitude)

    return return_list
