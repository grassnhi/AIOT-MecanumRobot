from mecanum import *
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
from yolobit import *
import machine
from i2c_motors_driver import DCMotor
import time

driver = DCMotor(machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000))

while True:
  x1 = mecanum.read_line_sensors(1)
  x2 = mecanum.read_line_sensors(2)
  x3 = mecanum.read_line_sensors(3)
  x4 = mecanum.read_line_sensors(4)
  display.set_all('#000000')
  if x1 == 0:
    display.set_pixel(1, 1, '#ff0000')
    driver.setSpeed(0,50)
    driver.setSpeed(1,50)
    driver.setSpeed(2,50)
    driver.setSpeed(3,50)
  else:
    display.set_pixel(1, 1, '#00ff00')
    driver.setSpeed(0,0)
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,0)
  if x2 == 0:
    display.set_pixel(2, 2, '#ff0000')
    driver.setSpeed(0,(-50))
    driver.setSpeed(1,(-50))
    driver.setSpeed(2,(-50))
    driver.setSpeed(3,(-50))
  else:
    display.set_pixel(2, 2, '#00ff00')
    driver.setSpeed(0,50)
    driver.setSpeed(1,50)
    driver.setSpeed(2,50)
    driver.setSpeed(3,50)
  if x3 == 0:
    display.set_pixel(3, 3, '#ff0000')
    driver.setSpeed(0,0)
    driver.setSpeed(1,50)
    driver.setSpeed(2,50)
    driver.setSpeed(3,0)
  else:
    display.set_pixel(3, 3, '#00ff00')
  if x4 == 0:
    display.set_pixel(4, 4, '#ff0000')
  else:
    display.set_pixel(4, 4, '#00ff00')
  time.sleep_ms(100)