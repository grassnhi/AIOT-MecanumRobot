import music
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
from yolobit import *
import machine
from i2c_motors_driver import DCMotor
import time

driver = DCMotor(machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000))

def on_button_a_pressed():
# turn left
  driver.setSpeed(0,25)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,25)
  time.sleep_ms(1000)

button_a.on_pressed = on_button_a_pressed

def on_button_b_pressed():

  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)
  time.sleep_ms(1000)

button_b.on_pressed = on_button_b_pressed

if True:
  music.play(music.POWER_UP, wait=False)

while True:
    pass
