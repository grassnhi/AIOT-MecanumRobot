from mecanum import *
from yolobit import *
import machine
from i2c_motors_driver import DCMotor
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
import time
import math
from mqtt import *

# Mô tả hàm này...
def ki_E1_BB_83m_tra_line_ngang():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  cross_line = 0
  is_going_forward = 0
  if (mecanum.read_line_sensors(1)) and (mecanum.read_line_sensors(4)):
    cross_line = 1
  if (mecanum.read_line_sensors(1)) and (mecanum.read_line_sensors(3)):
    cross_line = 1
  if (mecanum.read_line_sensors(2)) and (mecanum.read_line_sensors(4)):
    cross_line = 1
  if mecanum.read_line_sensors() == (0, 1, 1, 1):
    cross_line = 1
  if mecanum.read_line_sensors() == (1, 1, 1, 0):
    cross_line = 1
  if mecanum.read_line_sensors() == (1, 1, 1, 1):
    cross_line = 1
  if not cross_line:
    is_going_forward = 1
  return cross_line

driver = DCMotor(machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000))

# Mô tả hàm này...
def _C4_91i_th_E1_BA_B3ng():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
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

# Mô tả hàm này...
def t_C3_ADnh_t_E1_BB_91c__C4_91_E1_BB_99_PID():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
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
def return2():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  while not ki_E1_BB_83m_tra_line_ngang():
    _C4_91i_th_E1_BA_B3ng()
  r_E1_BA_BD_tr_C3_A1i()
  while not ki_E1_BB_83m_tra_line_ngang():
    _C4_91i_th_E1_BA_B3ng()
  r_E1_BA_BD_tr_C3_A1i()

# Mô tả hàm này...
def _C4_91i_E1_BB_81u_khi_E1_BB_83n__C4_91_E1_BB_99ng_c_C6_A1():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  driver.setSpeed(0,right_speed)
  driver.setSpeed(1,left_speed)
  driver.setSpeed(2,left_speed)
  driver.setSpeed(3,right_speed)

# Mô tả hàm này...
def k_E1_BA_BFt_n_E1_BB_91i_sever():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  mqtt.connect_wifi('Thanh Lien', 'home1974')
  mqtt.connect_broker(server='mqtt.ohstem.vn', port=1883, username='AICam', password='')

# Mô tả hàm này...
def straight():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  while not ki_E1_BB_83m_tra_line_ngang():
    _C4_91i_th_E1_BA_B3ng()

# Mô tả hàm này...
def test_r_E1_BA_BD_ph_E1_BA_A3i():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  if ki_E1_BB_83m_tra_line_ngang():
    r_E1_BA_BD_ph_E1_BA_A3i()
    is_going_forward = 1
  elif not is_going_forward:
    r_E1_BA_BD_ph_E1_BA_A3i()
    is_going_forward = 1
  else:
    _C4_91i_th_E1_BA_B3ng()

# Mô tả hàm này...
def t_C3_ADnh_gi_C3_A1_tr_E1_BB_8B_PID():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  P_val = Kp * error
  I_val = Ki * (I_val + error)
  D_val = Kd * (error - previous)
  error = previous
  PID_val = P_val + (I_val + D_val)

# Mô tả hàm này...
def d_C3_B2_line_pid():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
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
def left():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  while not ki_E1_BB_83m_tra_line_ngang():
    _C4_91i_th_E1_BA_B3ng()
  r_E1_BA_BD_tr_C3_A1i()

# Mô tả hàm này...
def test_r_E1_BA_BD_tr_C3_A1i():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  if ki_E1_BB_83m_tra_line_ngang():
    r_E1_BA_BD_tr_C3_A1i()
    is_going_forward = 1
  elif not is_going_forward:
    r_E1_BA_BD_tr_C3_A1i()
    is_going_forward = 1
  else:
    _C4_91i_th_E1_BA_B3ng()

def on_mqtt_message_receive_callback__V2_(th_C3_B4ng_tin):
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  rec0 = th_C3_B4ng_tin
  prev_state = th_C3_B4ng_tin
  kh_E1_BB_9Fi_t_E1_BA_A1o_PID()
  th_E1_BB_B1c_hi_E1_BB_87n_AI()

# Mô tả hàm này...
def l_E1_BA_A5y_d_E1_BB_AF_li_E1_BB_87u_sever():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  mqtt.check_message()
  mqtt.on_receive_message('V2', on_mqtt_message_receive_callback__V2_)

# Mô tả hàm này...
def stop():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)

# Mô tả hàm này...
def kh_E1_BB_9Fi_t_E1_BA_A1o_c_C3_A1c_gi_C3_A1_tr_E1_BB_8B():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  is_going_forward = 1
  count = 0
  rec0 = '0'
  rec1 = '0'
  rec2 = '0'
  time_out = 0
  th_C3_B4ng_tin = '0'

# Mô tả hàm này...
def kh_E1_BB_9Fi_t_E1_BA_A1o_PID():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  Kp = 25
  Kd = 2.5
  Ki = 0
  previous = 0
  I_val = 0
  base_speed = 50

# Mô tả hàm này...
def background():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)

# Mô tả hàm này...
def test_v_C3_B2ng_tr_C3_A1i():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  if ki_E1_BB_83m_tra_line_ngang():
    while ki_E1_BB_83m_tra_line_ngang():
      driver.setSpeed(0,30)
      driver.setSpeed(1,30)
      driver.setSpeed(2,30)
      driver.setSpeed(3,30)
    if not ki_E1_BB_83m_tra_line_ngang():
      count = (count if isinstance(count, (int, float)) else 0) + 1
    if count == 2:
      count = 0
      r_E1_BA_BD_tr_C3_A1i()
    print(str(count))
  else:
    _C4_91i_th_E1_BA_B3ng()

# Mô tả hàm này...
def right():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  while not ki_E1_BB_83m_tra_line_ngang():
    _C4_91i_th_E1_BA_B3ng()
  r_E1_BA_BD_ph_E1_BA_A3i()

# Mô tả hàm này...
def r_E1_BA_BD_ph_E1_BA_A3i():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  while ki_E1_BB_83m_tra_line_ngang():
    driver.setSpeed(0,30)
    driver.setSpeed(1,30)
    driver.setSpeed(2,30)
    driver.setSpeed(3,30)
  while not ki_E1_BB_83m_tra_line_ngang():
    driver.setSpeed(0,(-30))
    driver.setSpeed(1,50)
    driver.setSpeed(2,50)
    driver.setSpeed(3,(-30))
    if mecanum.read_line_sensors(1):
      break
  while not ki_E1_BB_83m_tra_line_ngang():
    driver.setSpeed(0,(-30))
    driver.setSpeed(1,50)
    driver.setSpeed(2,50)
    driver.setSpeed(3,(-30))
    if mecanum.read_line_sensors(4):
      break
  while not ((mecanum.read_line_sensors(2)) or (mecanum.read_line_sensors(3))):
    driver.setSpeed(0,(-30))
    driver.setSpeed(1,30)
    driver.setSpeed(2,30)
    driver.setSpeed(3,(-30))
  kh_E1_BB_9Fi_t_E1_BA_A1o_PID()

# Mô tả hàm này...
def th_E1_BB_B1c_hi_E1_BB_87n_AI():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  if prev_state == 'straight':
    display.scroll('F')
    straight()
  elif prev_state == 'left':
    display.scroll('L')
    left()
  elif prev_state == 'right':
    display.scroll('R')
    right()
  elif prev_state == 'return':
    display.scroll('B')
    return2()
  elif prev_state == 'stop':
    display.show(Image.NO)
    stop()
  else:
    display.set_all('#ffffff')
    background()

# Mô tả hàm này...
def r_E1_BA_BD_tr_C3_A1i():
  global cross_line, left_speed, P_val, S1, is_going_forward, Kp, rec2, right_speed, I_val, S2, th_C3_B4ng_tin, count, Kd, time_out, rec1, error, D_val, S3, rec0, Ki, prev_state, previous, PID_val, S4, divider, base_speed
  while ki_E1_BB_83m_tra_line_ngang():
    driver.setSpeed(0,30)
    driver.setSpeed(1,30)
    driver.setSpeed(2,30)
    driver.setSpeed(3,30)
  while not ki_E1_BB_83m_tra_line_ngang():
    driver.setSpeed(0,40)
    driver.setSpeed(1,(-30))
    driver.setSpeed(2,(-30))
    driver.setSpeed(3,40)
    if mecanum.read_line_sensors(1):
      break
  while not ((mecanum.read_line_sensors(2)) or (mecanum.read_line_sensors(3))):
    driver.setSpeed(0,30)
    driver.setSpeed(1,(-30))
    driver.setSpeed(2,(-30))
    driver.setSpeed(3,30)
  kh_E1_BB_9Fi_t_E1_BA_A1o_PID()

if True:
  k_E1_BA_BFt_n_E1_BB_91i_sever()
  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)
  display.set_all('#ff0000')
  wait_for(lambda: (button_a.is_pressed()))
  display.set_all('#000000')
  kh_E1_BB_9Fi_t_E1_BA_A1o_PID()
  kh_E1_BB_9Fi_t_E1_BA_A1o_c_C3_A1c_gi_C3_A1_tr_E1_BB_8B()

while True:
  l_E1_BA_A5y_d_E1_BB_AF_li_E1_BB_87u_sever()
  time.sleep_ms(10)


if time_out <= 0 or rec1 != rec0:
  if rec0 == rec1 and rec0 == rec2:
    time_out = 200
    prev_state = th_C3_B4ng_tin
    th_E1_BB_B1c_hi_E1_BB_87n_AI()
  elif time_out <= 0:
    th_E1_BB_B1c_hi_E1_BB_87n_AI()
    time_out = 200
  else:
    time_out = time_out - 1
    driver.setSpeed(0,0)
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,0)
rec2 = rec1
rec1 = rec0
