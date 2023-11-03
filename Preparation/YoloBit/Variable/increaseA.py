from yolobit import *

button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
import time

def on_button_a_pressed():
  global count  #####
  count = (count if isinstance(count, (int, float)) else 0) + 1

button_a.on_pressed = on_button_a_pressed

if True:
  count = 0

while True:
  display.scroll(count)
  time.sleep_ms(1000)
