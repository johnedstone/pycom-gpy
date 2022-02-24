### Description
Using the GPy from Pycom.io to POST data to a REST API (in this case a [Django REST Framework](https://www.django-rest-framework.org/)

### Firmware
* Upgrade Pytrack 2 firmware as described at this [link](https://docs.pycom.io/updatefirmware/expansionboard/)
* Upgrade GPy as described at this [link, for USB](https://docs.pycom.io/updatefirmware/ltemodem/)
    * `sudo usermod -a -G dialout $USER` and reboot 
    * [Download and install __Atom and install Pymakr__ plugin](https://docs.pycom.io/gettingstarted/software/atom/)
    * attach Gpy to Pytrack v2.  Connect Pytrack v2 with USB and REPL should be available in Atom
    * Example:
    ```
    >>> import sqnsupgrade as ssqn
    >>> ssqn.info()
    <<< Welcome to the SQN3330 firmware updater [1.2.6] >>>
    >>> GPy with firmware version 1.20.2.r2
    Your modem is in application mode. Here is the current version:
    UE5.4.0.2
    LR5.4.1.0-50523

    IMEI: xxxxx
    ```
    * Currently no firmware upgrade is needed [as described here](https://docs.pycom.io/updatefirmware/ltemodem/)
    * If a firmware upgrade is required, then probably do `sudo apt install python3-serial` and [follow link's](https://docs.pycom.io/updatefirmware/ltemodem/) instructions

### References 
* [Pycom documentation](https://docs.pycom.io/)
* [The pyboard.py tool](https://docs.micropython.org/en/latest/reference/pyboard.py.html)
* Useful debugging: see Readme_debugging.md

### Commands to be used with pyboard.py as compared to the Atom editor
```
../../pyboard.py -f cp main.py :main.py && ../../pyboard.py -f cp lib/arduino_get_https.py :lib/arduino_get_https.py
../../pyboard.py -c "import machine;machine.reset()"
../../pyboard.py -f ls
```

### See related sketch
* [Arduino related sketches MKRGSM1400 (public)](https://github.com/johnedstone/mkrgsm1400-post-json-ssl)

<!---
# vim: ai et ts=4 sw=4 sts=4 nu
-->
