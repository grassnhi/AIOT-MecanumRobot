from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1

import time


count = 0
for count2 in range(10):
  display.scroll(count)
  count = (count if isinstance(count, (int, float)) else 0) + 1
  time.sleep_ms(100)
