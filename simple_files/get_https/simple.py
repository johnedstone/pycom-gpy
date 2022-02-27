import time
import socket
import ssl
from network import LTE
import machine

#HOST = "some-other.server.net" # Let's Encrypt certs - does not work
#HOST = "www.google.com" # works
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

#ss = ssl.wrap_socket(s)
ss = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='/flash/cert/ca.pem')
ss.connect(addr)
print('certs accepted')
