"""
Device:
    Gpy (firmware, latest: shipped with CAT-M1 5.4.1.0-50523) on
    Pytrack 2 (firmware, latest: pytrack2_v16.dfu)
"""
import time

from machine import RTC
from network import LTE

from helper_functions import (
    attach_lte,
    make_request,
    sync_time,
    convert_time,
    get_gps_info,
)

from helper_bme680 import (
    get_bme680_data,
)

sleeping = 3600 # 1 hour
#sleeping = 900 # 15 min
#sleeping = 60  # 1 min

rtc = RTC()
lte = LTE()
IMEI = lte.imei()

print('Starting "post_json_data project"')

attach_lte(lte)
print("Is lte attached and connected: {} and {}".format(lte.isattached(), lte.isconnected()))

# The following, uncommented, works fine
#print('bme680 data: {}'.format(get_bme680_data()))

startup_time = time.mktime(sync_time(rtc))

# The following, uncommented, throws the error listed below
# with both pinout configuration as described in breadboard.py
#print('bme680 data: {}'.format(get_bme680_data()))
"""
Traceback (most recent call last):
  File "main.py", line 42, in <module>
  File "/flash/lib/helper_bme680.py", line 20, in get_bme680_data
  File "/flash/lib/bme680.py", line 195, in temperature
TypeError: unsupported types for __mul__: 'NoneType', 'int'
"""

print('Startup time is {}'.format(startup_time))

while True:
    try:
        now = rtc.now()
        t0 = time.time()
        uptime = convert_time(time.mktime(now) - startup_time)
        coord = get_gps_info()
        print('coord: {}'.format(coord))
        make_request(uptime, IMEI, startup_time, coord)

        lte.deinit(reset=True)

        print(uptime)
        print("lte.deinit() completed")
        print("Current time is {}".format(now))
    
    except Exception as e:
        print("==== ERROR ==== making request, followed by lte.deinit(): {} ".format(e))

    time_expired = time.time() - t0
    real_sleep = (max(sleeping - time_expired, 0))
    print("sleep interval: {}, time_expired: {}, real_sleep: {}".format(sleeping, time_expired, real_sleep))
    time.sleep(real_sleep)

    ## Start over, no need to set startup_time
    try:
        lte.init()
        attach_lte(lte)
        print("Is lte attached and connected: {} and {}".format(lte.isattached(), lte.isconnected()))
        print("Is rtc synced: {}".format(rtc.synced()))
    except Exception as e:
        print("==== ERROR ==== starting over: {}".format(e))
        print("Reseting modem and trying again")
        lte.reset()
        lte.init()
        attach_lte(lte)
        print("Is lte attached and connected: {} and {}".format(lte.isattached(), lte.isconnected()))
        print("Is rtc synce: {}".format(rtc.synced()))

# vim: ai et ts=4 sts=4 sw=4 nu
