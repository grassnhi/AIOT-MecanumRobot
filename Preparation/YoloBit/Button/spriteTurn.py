from game import *
game.reset()

import time

from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1


def on_button_a_pressed():
  global sprite
  sprite.turn(0, 90)

button_a.on_pressed = on_button_a_pressed


def on_button_b_pressed():
  global sprite
  sprite.turn(1, 90)

button_b.on_pressed = on_button_b_pressed


if True:
  sprite = game.create_sprite(0, 0)

while True:
  sprite.move_by(1)
  sprite.bounce_if_on_edge()
  time.sleep_ms(1000)
