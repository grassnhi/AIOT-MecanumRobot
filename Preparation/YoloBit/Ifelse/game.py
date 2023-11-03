from game import *
game.reset()

import random

from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1

import time


if True:
  sprite = game.create_sprite(0, 0)
  fish = game.create_sprite((random.randint(1, 4)), (random.randint(1, 4)))
  fish.color = hex_to_rgb("#00ff00")


while True:
  if accelerometer.is_gesture("tilt_right"):
    sprite.dir = GAME_DIR_RIGHT
    sprite.move_by(1)

  if accelerometer.is_gesture("tilt_left"):
    sprite.dir = GAME_DIR_LEFT
    sprite.move_by(1)

  if accelerometer.is_gesture("tilt_up"):
    sprite.dir = GAME_DIR_TOP
    sprite.move_by(1)

  if accelerometer.is_gesture("tilt_down"):
    sprite.dir = GAME_DIR_BOTTOM
    sprite.move_by(1)

  if sprite.is_touching(fish):
    game.win()
    
  time.sleep_ms(200)
