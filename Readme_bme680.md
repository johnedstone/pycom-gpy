### Pinout for PyTrack v2, GPy, and bme680 (Adafruit)

####
* See most importantly [this test script](https://github.com/johnedstone/pycom-gpy/blob/main/simple_files/gps_bme680_test/lib/breadboard.py)
    * Run this breadboard with an empty main.py
    ```
    import breadboard
    breadboard.repl_test()
    # or
    import time
    for _ in range(10000):
        repl_test()
        time.sleep(600) # 10min
    ```
* See also [`simple_files/bme680/Readme.md`](https://github.com/johnedstone/pycom-gpy/tree/main/simple_files/bme680)

#### Pinout
* See header, for example, [for this test script](https://github.com/johnedstone/pycom-gpy/blob/main/simple_files/gps_bme680_test/lib/breadboard.py)

#### References
* https://github.com/robert-hh/BME680-Micropython
* https://docs.pycom.io/tutorials/hardware/i2c/ 
* https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/overview and following pages
* https://randomnerdtutorials.com/bme680-sensor-arduino-gas-temperature-humidity-pressure/ (Arduino / I2C)
* https://forum.micropython.org/viewtopic.php?t=8612
* https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/python-circuitpython

<!--
# vim: ai et ts=4 sw=4 sts=4 nu
-->
