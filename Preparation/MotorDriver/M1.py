import music

from yolobit import *

button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1

import machine

from i2c_motors_driver import DCMotor

import time

driver = DCMotor(machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000))


if True:
  music.play(music.POWER_UP, wait=False)

while True:
  driver.setSpeed(0,50)
  time.sleep_ms(1000)
  driver.setSpeed(0,0)
  time.sleep_ms(1000)
