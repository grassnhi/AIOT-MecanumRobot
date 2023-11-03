from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1

if True:
  # define count
  count = 0

while True:
  # show value of count to the screen
  display.scroll(count)
