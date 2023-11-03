from yolobit import *

button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1

import time


if True:
  count = 0

while True:
  # increase count by 1
  count = (count if isinstance(count, (int, float)) else 0) + 1
  # display
  display.scroll(count)
  # delay
  time.sleep_ms(1000)
