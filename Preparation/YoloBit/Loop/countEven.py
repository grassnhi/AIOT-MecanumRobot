from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
import time


# count from 0 to 10, step = 2 => even number
for i in range(0, 11, 2):
  display.scroll(i)
  time.sleep_ms(1000)
