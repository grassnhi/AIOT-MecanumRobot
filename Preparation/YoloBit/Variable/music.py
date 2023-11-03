from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1

import music
import time


def on_button_a_pressed():
  global count
  count = (count if isinstance(count, (int, float)) else 0) + 1
  music.play(['G3:1'], wait=True)

button_a.on_pressed = on_button_a_pressed


def on_button_b_pressed():
  global count
  count = (count if isinstance(count, (int, float)) else 0) + -1
  music.play(['G3:1'], wait=True)

button_b.on_pressed = on_button_b_pressed


def on_button_a_b_pressed():
  global count
  count = 0
  music.play(['G3:1'], wait=True)

button_a.on_pressed_ab = on_button_a_b_pressed; button_b.on_pressed_ab = -1;


if True:
  count = 0


while True:
  display.scroll(count)
  time.sleep_ms(100)
