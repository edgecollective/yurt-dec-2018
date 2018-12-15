import board
import busio
import digitalio
import time
import gc

from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

SLEEPTIME = 3

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.RFM9X_CS)
reset = digitalio.DigitalInOut(board.RFM9X_RST)
import adafruit_rfm9x
r = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

def send(message):
    r.send(message)
    
ow_bus = OneWireBus(board.D5)
time.sleep(1.)

ds18 = DS18X20(ow_bus, ow_bus.scan()[0])
#t=ds18.temperature
#print(t)

while True:
    gc.collect()
    led.value=True
    time.sleep(1)
    led.value=False
    time.sleep(1)
    try:
        #ds18 = DS18X20(ow_bus, ow_bus.scan()[0])
        t=ds18.temperature  
        msg=str(t)
        send(msg)
        print(msg)
        time.sleep(SLEEPTIME)
    except Exception as e:
        print(e)
    
