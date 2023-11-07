import music
from yolobit import *
import machine
from i2c_motors_driver import DCMotor
from mecanum import *
import time
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1

driver = DCMotor(machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000))

# Mô tả hàm này...
def _C4_91i_ngang2():
  driver.setSpeed(0,(-40))
  driver.setSpeed(1,40)
  driver.setSpeed(2,(-40))
  driver.setSpeed(3,40)

# Mô tả hàm này...
def d_C3_B2_line_tr_C6_B0_E1_BB_9Bc():
  if mecanum.read_line_sensors() == (1, 0, 0, 0):
    driver.setSpeed(0,50)
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,50)
    time.sleep_ms(100)
    driver.setSpeed(0,0)
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,0)
  elif mecanum.read_line_sensors() == (1, 1, 0, 0):
    driver.setSpeed(0,40)
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,40)
    time.sleep_ms(100)
    driver.setSpeed(0,0)
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,0)
  elif mecanum.read_line_sensors() == (0, 0, 0, 1):
    driver.setSpeed(0,0)
    driver.setSpeed(1,50)
    driver.setSpeed(2,50)
    driver.setSpeed(3,0)
    time.sleep_ms(100)
    driver.setSpeed(0,0)
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,0)
  elif mecanum.read_line_sensors() == (0, 0, 1, 1):
    driver.setSpeed(0,0)
    driver.setSpeed(1,40)
    driver.setSpeed(2,40)
    driver.setSpeed(3,0)
    time.sleep_ms(100)
    driver.setSpeed(0,0)
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,0)
  elif mecanum.read_line_sensors() == (0, 0, 0, 0):
    driver.setSpeed(0,(-30))
    driver.setSpeed(1,(-30))
    driver.setSpeed(2,(-30))
    driver.setSpeed(3,(-30))
    time.sleep_ms(100)
    driver.setSpeed(0,0)
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,0)
  else:
    driver.setSpeed(0,30)
    driver.setSpeed(1,30)
    driver.setSpeed(2,30)
    driver.setSpeed(3,30)

# Mô tả hàm này...
def _C4_91i_ngang():
  driver.setSpeed(0,40)
  driver.setSpeed(1,(-40))
  driver.setSpeed(2,40)
  driver.setSpeed(3,(-40))

# Mô tả hàm này...
def d_C3_B2_line_sau():
  if pin16.read_digital() == 0 and pin12.read_digital() == 1:
    driver.setSpeed(0,(-50))
    driver.setSpeed(1,(-50))
    driver.setSpeed(2,0)
    driver.setSpeed(3,0)
    time.sleep_ms(50)
    driver.setSpeed(0,0)
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,0)
  elif pin12.read_digital() == 0 and pin16.read_digital() == 1:
    driver.setSpeed(0,0)
    driver.setSpeed(1,0)
    driver.setSpeed(2,(-50))
    driver.setSpeed(3,(-50))
    time.sleep_ms(50)
    driver.setSpeed(0,0)
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,0)
  else:
    driver.setSpeed(0,(-40))
    driver.setSpeed(1,(-40))
    driver.setSpeed(2,(-40))
    driver.setSpeed(3,(-40))

if True:
  music.play(music.POWER_UP, wait=False)
  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)

while True:
  d_C3_B2_line_tr_C6_B0_E1_BB_9Bc()
