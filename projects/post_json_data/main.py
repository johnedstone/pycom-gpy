"""
Device:
    Gpy (firmware, latest: shipped with CAT-M1 5.4.1.0-50523) on
    Pytrack 2 (firmware, latest: pytrack2_v16.dfu)
    Not yet: Pysense 2 (firmware, latest: pysense2_v16.dfu)
"""
import time

from machine import RTC
from network import LTE
from pycoproc_2 import Pycoproc

from helper_functions import (
    attach_lte,
    make_request,
    sync_time,
    convert_time,
    get_gps_info,
    )


sleeping = 3600 # 1 hour
#sleeping = 900 # 15 min
#sleeping = 60  # 1 min

rtc = RTC()
lte = LTE()
IMEI = lte.imei()

print('Starting "post_json_data project"')

try:
    py = Pycoproc()
    if py.read_product_id() != Pycoproc.USB_PID_PYTRACK:
        raise Exception('Not a Pytrack')
    time.sleep(1)
except Exception as e:
    print("No Pytrack: {}".format(e))

attach_lte(lte)
print("Is lte attached and connected: {} and {}".format(lte.isattached(), lte.isconnected()))

startup_time = time.mktime(sync_time(rtc))
print('Startup time is {}'.format(startup_time))

while True:
    try:
        now = rtc.now()
        t0 = time.time()
        uptime = convert_time(time.mktime(now) - startup_time)
        coord = get_gps_info(py)
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
