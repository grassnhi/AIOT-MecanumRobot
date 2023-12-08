from mecanum import *
import math
from yolobit import *
import machine
from i2c_motors_driver import DCMotor
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1

# Mô tả hàm này...
def d_C3_B2_line():
  global S1, left_speed, Kp, error, S2, right_speed, Kd, P_val, S3, Ki, D_val, S4, PID_val, previous, I_val, divider
  S1 = mecanum.read_line_sensors(1)
  S2 = mecanum.read_line_sensors(2)
  S3 = mecanum.read_line_sensors(3)
  S4 = mecanum.read_line_sensors(4)
  S1 = -2 * S1
  S2 = -S2
  S4 = 2 * S4
  error = (S1 + S2) + (S3 + S4)

# Mô tả hàm này...
def ki_E1_BB_83m_tra():
  global S1, left_speed, Kp, error, S2, right_speed, Kd, P_val, S3, Ki, D_val, S4, PID_val, previous, I_val, divider
  left_speed = round(30 + PID_val)
  right_speed = round(30 - PID_val)
  if left_speed > 30:
    left_speed = 30
  if left_speed < -30:
    left_speed = -30
  if right_speed > 30:
    right_speed = 30
  if right_speed < -30:
    right_speed = -30

# Mô tả hàm này...
def c_C3_A0i__C4_91_E1_BA_B7t():
  global S1, left_speed, Kp, error, S2, right_speed, Kd, P_val, S3, Ki, D_val, S4, PID_val, previous, I_val, divider
  Kp = 0.05
  Kd = 0
  Ki = 0
  previous = 0
  divider = 1

driver = DCMotor(machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000))

# Mô tả hàm này...
def _C4_91i_E1_BB_81u_ch_E1_BB_89nh():
  global S1, left_speed, Kp, error, S2, right_speed, Kd, P_val, S3, Ki, D_val, S4, PID_val, previous, I_val, divider
  error = 0 - error
  P_val = Kp * error
  D_val = (Kd * (error + previous)) / divider
  I_val = Ki * (error * divider)
  PID_val = P_val + (I_val + D_val)
  previous = error

# Mô tả hàm này...
def _C4_91i_E1_BB_81u_khi_E1_BB_83n():
  global S1, left_speed, Kp, error, S2, right_speed, Kd, P_val, S3, Ki, D_val, S4, PID_val, previous, I_val, divider
  driver.setSpeed(0,right_speed)
  driver.setSpeed(1,left_speed)
  driver.setSpeed(2,left_speed)
  driver.setSpeed(3,right_speed)

if True:
  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)
  wait_for(lambda: (button_a.is_pressed()))
  c_C3_A0i__C4_91_E1_BA_B7t()

while True:
  d_C3_B2_line()
  _C4_91i_E1_BB_81u_ch_E1_BB_89nh()
  ki_E1_BB_83m_tra()
  _C4_91i_E1_BB_81u_khi_E1_BB_83n()
