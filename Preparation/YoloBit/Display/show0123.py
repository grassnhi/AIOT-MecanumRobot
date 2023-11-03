from yolobit import *

button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1

import time


while True:
  display.scroll(0)
  time.sleep_ms(1000)
  display.scroll(1)
  time.sleep_ms(1000)
  display.scroll(3)
  time.sleep_ms(1000)
