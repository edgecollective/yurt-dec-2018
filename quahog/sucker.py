import sdcard, os
import machine
from machine import Pin
from machine import SPI
import ujson as json
import urequests as requests

import time

def do_connect(essid,psswd):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(False)
        sta_if.active(True)
        sta_if.connect(essid, psswd)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def post_farmos(payload):
    try:
        r = requests.post(url,data=json.dumps(payload),headers=headers)
    except Exception as e:
        print(e)
        #r.close()
        return "timeout"
    else:
        r.close()
        print('Status', r.status_code)
        return "posted"
   

sck=Pin(16)
mosi=Pin(4)
miso=Pin(17)
cs = Pin(15, Pin.OUT)
spi2=SPI(2,baudrate=5000000,sck=sck,mosi=mosi,miso=miso)

sd = sdcard.SDCard(spi2, cs)
os.mount(sd,'/sd')

f=open('/sd/wifi_config.csv')
c=f.read()
essid=c.split(',')[0].strip()
psswd=c.split(',')[1].strip()
f.close()

f=open('/sd/farmos_config.csv')
c=f.read()
public_key=c.split(',')[0].strip()
private_key=c.split(',')[1].strip()
f.close()

base_url='https://wolfesneck.farmos.net/farm/sensor/listener/'
url = base_url+public_key+'?private_key='+private_key
headers = {'Content-type':'application/json', 'Accept':'application/json'}


do_connect(essid,psswd)
test_payload ={"test":3.3}

post_farmos(test_payload)




