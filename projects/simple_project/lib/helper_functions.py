import time
import socket
import ssl
import re
import json

import machine
import private_vars

def convert_time(seconds):
    """
    https://www.tutsmake.com/python-convert-time-in-seconds-to-days-hours-minutes-seconds/
    """
    try:
        total_seconds = seconds
        days = seconds // (24 * 3600)
        seconds = seconds % (24 * 3600)
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
    
        return "uptime: {:00d}d {:02d}:{:02d}:{:02d} or {:00d}s".format(
            days, hours, minutes, seconds, total_seconds)
    except Exception as e:
        print("convert_time error: {}".format(e))
        return "uptime: unknown, convert_time error"


def sync_time(rtc):
    try:
        print(time.localtime())
    
        rtc.ntp_sync("pool.ntp.org")
    
        rtc_status = rtc.synced()
        while not rtc_status:
            rtc_status = rtc.synced()
            print("rtc_status: {}".format(rtc_status))
            time.sleep(1)
    
        startup_time = time.localtime()
        print("RTC synced with NTP time: {}".format(startup_time))
        # epoch time
        return time.time()

    except Exception as e:
        print("convert_time error: {}".format(e))
        # epoch time in the distant future
        return 9999999999 


def attach_lte(lte):
    try:
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
    except Exception as e:
        print("attach_lte error: {}".format(e))


def get_IMEI(lte, IMEI):
    try:
        if re.search('[^a-zA-Z0-9]', IMEI):
            print("IMEI is garbage: ".format(IMEI))
            IMEI = ""

        if IMEI:
            return IMEI

        while not IMEI:
            try:
                IMEI = lte.imei()
                time.sleep(1.25)
            except OSError as e:
                """
                https://github.com/pycom/pycom-micropython-sigfox/issues/188
                """
                print("get_IMEI error #1: {}".format(e))
                lte.disconnect()
                lte.pppsuspend()

        lte.pppresume()
        return IMEI

    except Exception as e:
        print("get_IMEI error #2: {}".format(e))


def make_request (uptime, IMEI):
    try:
        posting = json.dumps({
            'uptime': uptime,
            'imei_string': IMEI,
            })

        s = socket.socket()
        ai = socket.getaddrinfo(private_vars.HOST, 443)
        addr = ai[0][-1]
        
        path = private_vars.PATH
        host = private_vars.HOST
        
        ss = ssl.wrap_socket(s)
        #ss = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='/flash/cert/ca.pem')
        ss.connect(addr)
        
        #ss.write(b"GET {} HTTP/1.0\r\n{}\r\nConnection:close\r\n\r\n".format(path, host))
        ss.write(b"POST ")
        ss.write(b"{}".format(path))
        ss.write(b" HTTP/1.1\r\n")
        ss.write(b"HOST: {}\r\n".format(host))

        #}Connection:close\r\n\r\n".format(path, host))

        ss.write(b"Content-Type: application/json;charset=UTF-8\r\n")
        ss.write(b"Connection: close\r\n")
        ss.write(b"Content-Length: ")
        ss.write(b'{}\r\n'.format(len(posting)))

        # Terminate headers
        ss.write(b'\r\n')
        ss.send(posting)
        
        #print(ss.read(4096))
    
        data = ss.read(4096)
        ss.close()

        print("{}".format(json.loads(posting)))
    
        for l in data.decode('utf-8').split('\r\n'):
            print(l)
        
        print("Request complete, good night ...")
    except Exception as e:
        print("make_request error: {}".format(e))

# vim: ai et ts=4 sw=4 sts=4 nu