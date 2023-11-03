from yolobit import *

button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1


def on_button_a_pressed():
  global sprite
  display.show(Image.HAPPY)

button_a.on_pressed = on_button_a_pressed


def on_button_b_pressed():
  global sprite
  display.show(Image.SAD)

button_b.on_pressed = on_button_b_pressed


def on_button_a_b_pressed():
  global sprite
  display.show(Image.NO)

button_a.on_pressed_ab = on_button_a_b_pressed; button_b.on_pressed_ab = -1;


if True:
  display.clear()

while True:
    pass
