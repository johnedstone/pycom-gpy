from network import WLAN
import time
import machine

wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid="", auth=(WLAN.WPA2, "")) #for the connection details, check your router.
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

#while True:
if 1 == 1:
    print(time.localtime())
    time.sleep(1)
