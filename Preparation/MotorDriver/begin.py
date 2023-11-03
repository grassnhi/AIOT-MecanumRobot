import music

from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1

import time

from yolobit import *

import machine

from i2c_motors_driver import DCMotor


driver = DCMotor(machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000))


if True:
  music.play(music.POWER_UP, wait=False)


while True:
  display.show(Image.HEART)
  time.sleep_ms(1000)

  display.show(Image.SMILE)
  time.sleep_ms(1000)
  # run for test
  driver.setSpeed(0,50)
  driver.setSpeed(1,50)
  driver.setSpeed(2,50)
  driver.setSpeed(3,50)
  time.sleep_ms(1000)
  # Stop 
  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)
