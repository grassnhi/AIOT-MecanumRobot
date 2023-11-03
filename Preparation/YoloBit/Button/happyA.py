from yolobit import *

button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1


def on_button_a_pressed():
  global sprite
  display.show(Image.HAPPY)

# A is pressed -> display happy
button_a.on_pressed = on_button_a_pressed

if True:
  display.clear()

while True:
    pass
