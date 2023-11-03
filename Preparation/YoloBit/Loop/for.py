from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
import time

# count from 1 to 10
for i in range(1, 11):
  display.scroll(i)
  time.sleep_ms(1000)

# count from 0 to 10
for i in range(11):
  display.scroll(i)
  time.sleep_ms(1000)

# count from 0 to 9
for i in range(10):
  display.scroll(i)
  time.sleep_ms(1000)