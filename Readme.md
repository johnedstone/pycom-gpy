### Description
Using the GPy from Pycom.io to POST data to a REST API (in this case a [Django REST Framework](https://www.django-rest-framework.org/)
* Using a Hologram.io SIM

### Currently (unfinished)
Currently working on `post_json_data` in projects folder

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
Sometimes Atom and the Pymakr plugin do not always work, e.g. failed to upload.
Resolve these type of issues after downloading [pyboard.py](./pyboard.py simple_files/get_https/main.py)
and using the virtual environment (see Pipfile).  Some examples are below.

```
#Cleaning up
./pyboard.py -f rm :main.py
rm :main.py

./pyboard.py -f ls :
ls :
          29 boot.py
           0 cert/
           0 lib/
          34 main.py
           0 sys/

#Default main.py
./pyboard.py -f cat :main.py
cat :main.py
# main.py -- put your code here!

#Run this script in memory
./pyboard.py simple_files/hello_world/main.py
Hello!
Hello!

#Run this project in memory after loading libraries
./pyboard.py -f cp projects/hello_world/lib/helper_functions.py :lib/
cp projects/hello_world/lib/helper_functions.py :lib/helper_functions.py

./pyboard.py -f cat :lib/helper_functions.py
cat :lib/helper_functions.py
import private_vars

def hello_world():
    return '{}'.format(private_vars.msg)

./pyboard.py projects/hello_world/main.py
Starting "Hello World Project"
msg: Goodnight Moon!
msg: Goodnight Moon!
msg: Goodnight Moon!

#Another example of testing a script before uploading it
./pyboard.py simple_files/get_https/main.py

```
### Serial connections.
In addition to the `pyboard.py` tool (above), one can enter the REPL with a serial connection

For example:
```
screen /dev/ttyACM0 115200
#or,
screen /dev/ttyACM0 115200 -hupc

#Or, starting with pyboard
./pyboard.py --no-exclusive simple_files/hello_world/main.py
#then, Ctrl-C, exiting, and then to follow the output
screen /dev/ttyACM0 115200 -hupc
#and to drop to a python prompt: Ctrl-C Ctrl-B
>>>
>>> help()

```

### See related sketch
* [Arduino related sketches MKRGSM1400 (public)](https://github.com/johnedstone/mkrgsm1400-post-json-ssl)

<!---
# vim: ai et ts=4 sw=4 sts=4 nu
-->
