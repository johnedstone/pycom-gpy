'''
https://docs.pycom.io/tutorials/networkprotocols/ntp/
'''
from network import WLAN
import time
import machine
import private_vars

wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid='{}'.format(private_vars.SSID), auth=(WLAN.WPA2, '{}'.format(private_vars.SSID_PASSWORD))) #for the connection details, check your router.

while not wlan.isconnected():
    machine.idle()
print("connected to WiFi")
rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
while not rtc.synced():
    machine.idle()
print("RTC synced with NTP time")
#adjust your local timezone, by default, NTP time will be GMT
time.timezone(2*60**2) #we are located at GMT+2, thus 2*60*60

while True:
    print(time.localtime())
    print(rtc.now())
    time.sleep(1)

# vim: ai et ts=4 sts=4 sw=4 nu
