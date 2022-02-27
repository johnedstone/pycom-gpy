"""
https://zetcode.com/python/socket/
https://forum.pycom.io/topic/954/send-data-requests-http-post-solved
"""
import time
import socket
import ssl
from network import LTE
import machine

HOST = "some-another.server.net" # Let's Encrypt - does not work
HOST = "www.google.com" # works
HOST = "www.example.org" # works

lte = LTE()
lte.attach()
print("attaching..",end='')
while not lte.isattached():
    time.sleep(0.25)

    print('.',end='')
    print(lte.send_at_cmd('AT!="fsm"'))         # get the System FSM
print("attached!")

lte.connect()
print("connecting [##",end='')
while not lte.isconnected():
    time.sleep(0.25)
    print('#',end='')
    #print(lte.send_at_cmd('AT!="showphy"'))
    print(lte.send_at_cmd('AT!="fsm"'))
print("] connected!")

s = socket.socket()

ai = socket.getaddrinfo('{}'.format(HOST), 443)
addr = ai[0][-1]

path = "/"
host = 'HOST: {}'.format(HOST)

#ss = ssl.wrap_socket(s)
ss = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='/flash/cert/ca.pem')
ss.connect(addr)

ss.write(b"GET {} HTTP/1.0\r\n{}\r\nConnection:close\r\n\r\n".format(path, host))

print(ss.read(4096))

ss.close()
#lte.deinit()

print("Done, good night ...")

rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
rtc_status = rtc.synced()
while not rtc_status:
    rtc_status = rtc.synced()
    print("rtc_status: {}".format(rtc_status))
    print("This may take several minutes - be patient")
    time.sleep(1)

print("RTC synced with NTP time")

while True:
    print(time.localtime())
    print(rtc.synced())
    time.sleep(5)

# vim: ai et ts=4 sts=4 sw=4 nu
