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

<!---
# vim: ai et ts=4 sw=4 sts=4 nu
-->
