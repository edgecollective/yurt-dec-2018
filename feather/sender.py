import board
import busio
import digitalio
import time

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.RFM9X_CS)
reset = digitalio.DigitalInOut(board.RFM9X_RST)
import adafruit_rfm9x
r = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT


def send(message):
    r.send(message)
    
def receive(timeout):
    result=r.receive(timeout=timeout)
    return result
    
while True:
    led.value=True
    time.sleep(1)
    led.value=False
    time.sleep(1)
    msg='hallo!'
    send(msg)
    print(msg)
    
