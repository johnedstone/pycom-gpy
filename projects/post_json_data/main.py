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


sleeping = 3600 - 30 # 1 hour
#sleeping = 900 - 30 # 15 min
#sleeping = 60 # 1 min

rtc = RTC()
lte = LTE()
IMEI = lte.imei()

choices = { 1: 'pytrack',
            2: 'pysense',
            3: 'other',
          }

report_choice = choices[1]

print('Starting "post_json_data project"')

attach_lte(lte)
print("Is lte attached and connected: {} and {}".format(lte.isattached(), lte.isconnected()))

startup_time = time.mktime(sync_time(rtc))
print('Startup time is {}'.format(startup_time))

while True:
    try:
        now = rtc.now()
        uptime = convert_time(time.mktime(now) - startup_time)
        coord = get_gps_info(report_choice)
        make_request(uptime, IMEI, startup_time, coord)
    
        lte.deinit(reset=True)

        print(uptime)
        print("lte.deinit() completed")
        print("Current time is {}".format(now))
    
        print("Sleeping for {} min {} sec".format(sleeping // 60, sleeping % 60))
    except Exception as e:
        print("error making request and then lte.deinit(): {} ".format(e))

    time.sleep(sleeping)

    ## Start over, no need to set startup_time
    try:
        lte.init()
        attach_lte(lte)
        print("Is lte attached and connected: {} and {}".format(lte.isattached(), lte.isconnected()))
        print("Is rtc synced: {}".format(rtc.synced()))
    except Exception as e:
        print("error starting over: {}".format(e))
        print("Reseting modem and trying again")
        lte.reset()
        lte.init()
        attach_lte(lte)
        print("Is lte attached and connected: {} and {}".format(lte.isattached(), lte.isconnected()))
        print("Is rtc synce: {}".format(rtc.synced()))

# vim: ai et ts=4 sts=4 sw=4 nu
