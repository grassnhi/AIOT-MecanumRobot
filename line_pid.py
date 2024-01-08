import math
from mecanum import *
from yolobit import *
import machine
from i2c_motors_driver import DCMotor
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
import time
from mqtt import *

# Mô tả hàm này...
def t_C3_ADnh_t_E1_BB_91c__C4_91_E1_BB_99_PID():
  global left_speed, cross_line, P_val, S1, count, Kp, right_speed, I_val, S2, th_C3_B4ng_tin, Kd, error, D_val, S3, Ki, PID_val, previous, S4, divider, base_speed
  left_speed = round(50 - PID_val)
  right_speed = round(50 + PID_val)
  if left_speed >= 50:
    left_speed = 50
  elif left_speed <= -50:
    left_speed = -50
  if right_speed >= 50:
    right_speed = 50
  elif right_speed <= -50:
    right_speed = -50

# Mô tả hàm này...
def ki_E1_BB_83m_tra_line_ngang():
  global left_speed, cross_line, P_val, S1, count, Kp, right_speed, I_val, S2, th_C3_B4ng_tin, Kd, error, D_val, S3, Ki, PID_val, previous, S4, divider, base_speed
  cross_line = 0
  if mecanum.read_line_sensors() == (1, 1, 1, 1):
    cross_line = 1
  if mecanum.read_line_sensors() == (1, 0, 0, 1):
    cross_line = 1
  if mecanum.read_line_sensors() == (1, 1, 1, 0):
    cross_line = 1
  if mecanum.read_line_sensors() == (0, 1, 1, 1):
    cross_line = 1
  if mecanum.read_line_sensors() == (1, 0, 1, 0):
    cross_line = 1
  if mecanum.read_line_sensors() == (0, 1, 0, 1):
    cross_line = 1
  return cross_line

# Mô tả hàm này...
def _C4_91i_th_E1_BA_B3ng():
  global left_speed, cross_line, P_val, S1, count, Kp, right_speed, I_val, S2, th_C3_B4ng_tin, Kd, error, D_val, S3, Ki, PID_val, previous, S4, divider, base_speed
  while mecanum.read_line_sensors() == (0, 0, 0, 0):
    if previous > 0:
      left_speed = -30
      right_speed = 30
      _C4_91i_E1_BB_81u_khi_E1_BB_83n__C4_91_E1_BB_99ng_c_C6_A1()
    else:
      left_speed = 30
      right_speed = -30
      _C4_91i_E1_BB_81u_khi_E1_BB_83n__C4_91_E1_BB_99ng_c_C6_A1()
  d_C3_B2_line_pid()
  t_C3_ADnh_gi_C3_A1_tr_E1_BB_8B_PID()
  t_C3_ADnh_t_E1_BB_91c__C4_91_E1_BB_99_PID()
  _C4_91i_E1_BB_81u_khi_E1_BB_83n__C4_91_E1_BB_99ng_c_C6_A1()

driver = DCMotor(machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000))

# Mô tả hàm này...
def _C4_91i_E1_BB_81u_khi_E1_BB_83n__C4_91_E1_BB_99ng_c_C6_A1():
  global left_speed, cross_line, P_val, S1, count, Kp, right_speed, I_val, S2, th_C3_B4ng_tin, Kd, error, D_val, S3, Ki, PID_val, previous, S4, divider, base_speed
  driver.setSpeed(0,right_speed)
  driver.setSpeed(1,left_speed)
  driver.setSpeed(2,left_speed)
  driver.setSpeed(3,right_speed)

# Mô tả hàm này...
def t_C3_ADnh_gi_C3_A1_tr_E1_BB_8B_PID():
  global left_speed, cross_line, P_val, S1, count, Kp, right_speed, I_val, S2, th_C3_B4ng_tin, Kd, error, D_val, S3, Ki, PID_val, previous, S4, divider, base_speed
  P_val = Kp * error
  I_val = Ki * (I_val + error)
  D_val = Kd * (error - previous)
  error = previous
  PID_val = P_val + (I_val + D_val)

# Mô tả hàm này...
def d_C3_B2_line_pid():
  global left_speed, cross_line, P_val, S1, count, Kp, right_speed, I_val, S2, th_C3_B4ng_tin, Kd, error, D_val, S3, Ki, PID_val, previous, S4, divider, base_speed
  S1 = mecanum.read_line_sensors(1)
  S2 = mecanum.read_line_sensors(2)
  S3 = mecanum.read_line_sensors(3)
  S4 = mecanum.read_line_sensors(4)
  divider = (S1 + S2) + (S3 + S4)
  if divider <= 0:
    divider = 1
  S1 = 0 * S1
  S1 = 1 * S2
  S1 = 2 * S3
  S1 = 3 * S4
  error = (S1 + S2) + (S3 + S4)
  error = 2.5 - error
  error = error / divider

# Mô tả hàm này...
def k_E1_BA_BFt_n_E1_BB_91i_sever():
  global left_speed, cross_line, P_val, S1, count, Kp, right_speed, I_val, S2, th_C3_B4ng_tin, Kd, error, D_val, S3, Ki, PID_val, previous, S4, divider, base_speed
  mqtt.connect_wifi('wifi', 'password')
  mqtt.connect_broker(server='mqtt.ohstem.vn', port=1883, username='', password='')

def on_mqtt_message_receive_callback__topic_(th_C3_B4ng_tin):
  global left_speed, cross_line, P_val, S1, count, Kp, right_speed, I_val, S2, Kd, error, D_val, S3, Ki, PID_val, previous, S4, divider, base_speed
  pass

# Mô tả hàm này...
def l_E1_BA_A5y_d_E1_BB_AF_li_E1_BB_87u_sever():
  global left_speed, cross_line, P_val, S1, count, Kp, right_speed, I_val, S2, th_C3_B4ng_tin, Kd, error, D_val, S3, Ki, PID_val, previous, S4, divider, base_speed
  mqtt.check_message()
  mqtt.on_receive_message('topic', on_mqtt_message_receive_callback__topic_)

# Mô tả hàm này...
def kh_E1_BB_9Fi_t_E1_BA_A1o_c_C3_A1c_gi_C3_A1_tr_E1_BB_8B():
  global left_speed, cross_line, P_val, S1, count, Kp, right_speed, I_val, S2, th_C3_B4ng_tin, Kd, error, D_val, S3, Ki, PID_val, previous, S4, divider, base_speed
  count = 0

# Mô tả hàm này...
def kh_E1_BB_9Fi_t_E1_BA_A1o_PID():
  global left_speed, cross_line, P_val, S1, count, Kp, right_speed, I_val, S2, th_C3_B4ng_tin, Kd, error, D_val, S3, Ki, PID_val, previous, S4, divider, base_speed
  Kp = 25
  Kd = 2.5
  Ki = 0
  previous = 0
  I_val = 0
  base_speed = 50

# Mô tả hàm này...
def r_E1_BA_BD_tr_C3_A1i():
  global left_speed, cross_line, P_val, S1, count, Kp, right_speed, I_val, S2, th_C3_B4ng_tin, Kd, error, D_val, S3, Ki, PID_val, previous, S4, divider, base_speed
  while ki_E1_BB_83m_tra_line_ngang():
    driver.setSpeed(0,30)
    driver.setSpeed(1,30)
    driver.setSpeed(2,30)
    driver.setSpeed(3,30)
  while not (mecanum.read_line_sensors(4)):
    driver.setSpeed(0,30)
    driver.setSpeed(1,(-20))
    driver.setSpeed(2,(-20))
    driver.setSpeed(3,30)
  while mecanum.read_line_sensors(2):
    driver.setSpeed(0,(-20))
    driver.setSpeed(1,20)
    driver.setSpeed(2,20)
    driver.setSpeed(3,(-20))
  kh_E1_BB_9Fi_t_E1_BA_A1o_PID()

# Mô tả hàm này...
def r_E1_BA_BD_ph_E1_BA_A3i():
  global left_speed, cross_line, P_val, S1, count, Kp, right_speed, I_val, S2, th_C3_B4ng_tin, Kd, error, D_val, S3, Ki, PID_val, previous, S4, divider, base_speed
  while ki_E1_BB_83m_tra_line_ngang():
    driver.setSpeed(0,30)
    driver.setSpeed(1,30)
    driver.setSpeed(2,30)
    driver.setSpeed(3,30)
  while not (mecanum.read_line_sensors(1)):
    driver.setSpeed(0,(-20))
    driver.setSpeed(1,30)
    driver.setSpeed(2,30)
    driver.setSpeed(3,(-20))
  while mecanum.read_line_sensors(3):
    driver.setSpeed(0,20)
    driver.setSpeed(1,(-20))
    driver.setSpeed(2,(-20))
    driver.setSpeed(3,(-20))
  kh_E1_BB_9Fi_t_E1_BA_A1o_PID()

if True:
  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)
  wait_for(lambda: (button_a.is_pressed()))
  kh_E1_BB_9Fi_t_E1_BA_A1o_PID()
  kh_E1_BB_9Fi_t_E1_BA_A1o_c_C3_A1c_gi_C3_A1_tr_E1_BB_8B()

while True:
  if ki_E1_BB_83m_tra_line_ngang():
    while ki_E1_BB_83m_tra_line_ngang():
      cross_line = cross_line + 1
    if cross_line >= 0:
      cross_line = 0
      count = count + 1
    if count > 1:
      count = 0
      r_E1_BA_BD_tr_C3_A1i()
    print(str(count))
  else:
    _C4_91i_th_E1_BA_B3ng()
  time.sleep_ms(10)
