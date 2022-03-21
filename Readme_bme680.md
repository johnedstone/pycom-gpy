### Pinout for PyTrack v2, GPy, and (Adafruit) bme680
#### Pytrack v2 and GPy
J5 Pytrack and see GPy minimal required circuit:
* #1: (first) reset
* #2 and #3: Rx/Tx
* #14 (last) Safe boot button

J6 Pytrack and see GPy minimal required circuit:
* #1 (first) 5V
* #2 3.3 V out
* #3 Ground
* #5 and #6: SDA/SDL (IC2)
* #12, #13, #14: (last) not sure these are needed (see documentation)


### References
* https://github.com/robert-hh/BME680-Micropython
* https://docs.pycom.io/tutorials/hardware/i2c/ 
* https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/overview and following pages
* https://randomnerdtutorials.com/bme680-sensor-arduino-gas-temperature-humidity-pressure/ (Arduino / I2C)

<!--
# vim: ai et ts=4 sw=4 sts=4 nu
-->
