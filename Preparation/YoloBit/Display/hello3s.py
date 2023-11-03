from yolobit import *

button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1

import time

while True:
  display.scroll('Hello')
  time.sleep_ms(3000)
