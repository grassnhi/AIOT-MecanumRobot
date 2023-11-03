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
    # if status = tilted to the right
    if accelerometer.is_gesture("tilt_right"):
        # sprite turn right
        sprite.dir = GAME_DIR_RIGHT
        # move by 1 step
        sprite.move_by(1)
    # delay
    time.sleep_ms(200)
