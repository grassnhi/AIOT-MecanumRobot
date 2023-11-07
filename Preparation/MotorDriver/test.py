import music
from ble import *
from yolobit import *
import machine
from i2c_motors_driver import DCMotor
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
import time

driver = DCMotor(machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000))

def on_ble_message_string_receive_callback(chu_E1_BB_97i):

  if chu_E1_BB_97i == ('!B516'):
    driver.setSpeed(0,50)
    driver.setSpeed(1,50)
    driver.setSpeed(2,50)
    driver.setSpeed(3,50)
  elif chu_E1_BB_97i == ('!B615'):
    driver.setSpeed(0,(-50))
    driver.setSpeed(1,(-50))
    driver.setSpeed(2,(-50))
    driver.setSpeed(3,(-50))
  elif chu_E1_BB_97i == ('!B714'):
    driver.setSpeed(0,30)
    driver.setSpeed(1,(-30))
    driver.setSpeed(2,(-30))
    driver.setSpeed(3,30)
  elif chu_E1_BB_97i == ('!B814'):
    driver.setSpeed(0,(-30))
    driver.setSpeed(1,30)
    driver.setSpeed(2,30)
    driver.setSpeed(3,(-30))
  elif chu_E1_BB_97i == ('!B11:'):
    pin0.servo_write(90)
    time.sleep_ms(1000)
    pin1.servo_write(90)
    music.play(['G3:1'], wait=True)
  elif chu_E1_BB_97i == ('!B219'):
    pin0.servo_write(0)
    time.sleep_ms(1000)
    pin1.servo_write(0)
  elif chu_E1_BB_97i == ('!B318'):
    pin8.servo_write(0)
    time.sleep_ms(1000)
    pin9.servo_write(0)
  elif chu_E1_BB_97i == ('!B417'):
    pin8.servo_write(90)
    time.sleep_ms(1000)
    pin9.servo_write(90)
  else:
    driver.setSpeed(0,0)
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,0)

ble.on_receive_msg("string", on_ble_message_string_receive_callback)

def on_ble_message_string_receive_callback(chu_E1_BB_97i):

  if chu_E1_BB_97i == ('!B516'):
    driver.setSpeed(0,50)
    driver.setSpeed(1,50)
    driver.setSpeed(2,50)
    driver.setSpeed(3,50)
  elif chu_E1_BB_97i == ('!B615'):
    driver.setSpeed(0,(-50))
    driver.setSpeed(1,(-50))
    driver.setSpeed(2,(-50))
    driver.setSpeed(3,(-50))
  elif chu_E1_BB_97i == ('!B714'):
    driver.setSpeed(0,30)
    driver.setSpeed(1,(-30))
    driver.setSpeed(2,(-30))
    driver.setSpeed(3,30)
  elif chu_E1_BB_97i == ('!B814'):
    driver.setSpeed(0,(-30))
    driver.setSpeed(1,30)
    driver.setSpeed(2,30)
    driver.setSpeed(3,(-30))
  elif chu_E1_BB_97i == ('!B11:'):
    pin0.servo_write(90)
    time.sleep_ms(1000)
    pin1.servo_write(90)
    music.play(['G3:1'], wait=True)
  elif chu_E1_BB_97i == ('!B219'):
    pin0.servo_write(0)
    time.sleep_ms(1000)
    pin1.servo_write(0)
  elif chu_E1_BB_97i == ('!B318'):
    pin8.servo_write(0)
    time.sleep_ms(1000)
    pin9.servo_write(0)
  elif chu_E1_BB_97i == ('!B417'):
    pin8.servo_write(90)
    time.sleep_ms(1000)
    pin9.servo_write(90)
  else:
    driver.setSpeed(0,0)
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,0)

ble.on_receive_msg("string", on_ble_message_string_receive_callback)

if True:
  music.play(music.POWER_UP, wait=False)

while True:
    pass
