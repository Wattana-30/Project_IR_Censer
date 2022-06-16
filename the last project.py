from machine import UART, Pin, PWM
import machine
import _thread
import time
import utime
from machine import I2C, Pin, SPI
from mfrc522 import MFRC522
from sg90 import Servo
from time import sleep

ir = Pin(9,Pin.IN)
led_red = Pin(12,Pin.OUT)
true = Pin(15, Pin.OUT)
false = Pin(14, Pin.OUT)
sck = Pin(6, Pin.OUT)
mosi = Pin(7, Pin.OUT)
miso = Pin(4, Pin.OUT)
sda = Pin(5, Pin.OUT)
rst = Pin(22, Pin.OUT)
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
card1 = "0x1210711b"
card2 = "0x4b67032e"
buzzer = PWM(Pin(18))
servo = Servo(26)
trigger = Pin(21, Pin.OUT)
echo = Pin(10, Pin.IN)
servo1 = Servo(27)


def pippip():
    for i in range(2):
         buzzer.duty_u16(900000)
         utime.sleep_ms(100)
         buzzer.duty_u16(0)
         utime.sleep_ms(100)
         
def pippip1():
    for i in range(5):
         buzzer.duty_u16(900000)
         utime.sleep_ms(100)
         buzzer.duty_u16(0)
         utime.sleep_ms(100)
         
def card_scan():
    rdr = MFRC522(spi, sda, rst)
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
            print(uid)
            if uid == card1:
                true.toggle()
                time.sleep(1)
                pippip()
                servo_on()
               
            elif uid == card2:
                true.toggle()
                time.sleep(1)
                pippip1()
            else:
                false.value(1)
                time.sleep(0.1)
                false.value(0)
                time.sleep(0.1)
                false.value(1)
                time.sleep(0.1)
                false.value(0)
                time.sleep(0.1)
                false.value(1)
                time.sleep(0.1)
                false.value(0)
                time.sleep(1)

def servo_on():
    servo.setServo90()
    time.sleep(3)

def servo_off():
    servo.setServo0()
    time.sleep(3)
    
def servo1_on():
    servo.setServo90()
    time.sleep(3)


def servo1_off():
    servo.setServo0()
    time.sleep(3)


while True:
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print("The distance from object is" ,distance,"cm")
    utime.sleep(0.5)
    card_scan()
    
    if ir.value() == 0:
        led_red.high()
        print("ON")
        if (distance) <= 20:
            servo1_on()
            
        else:
            servo1_off()
            
    else:
        led_red.low()
        print("OFF")
        servo_off()
        

      