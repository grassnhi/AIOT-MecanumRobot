from game import *

game.reset()


if True:
  sprite = game.create_sprite(2, 2)

while True:
  sprite.color = hex_to_rgb("#00ff00")
  sprite.blink = 1
