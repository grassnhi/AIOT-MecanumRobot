from game import *
game.reset()

import random

if True:
  # create sprite at 0,0
  sprite = game.create_sprite(0, 0)
  # random fish location
  fish = game.create_sprite((random.randint(1, 4)), (random.randint(1, 4)))
  # change color to identify
  fish.color = hex_to_rgb("#00ff00")

while True:
    pass
