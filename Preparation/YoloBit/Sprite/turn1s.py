from game import *
game.reset()

import time

if True:
  sprite = game.create_sprite(0, 0)

while True:
  sprite.move_by(4)
  sprite.turn(1, 90)
  time.sleep_ms(1000)


#   sprite.move_by(1)               # move 1 step
#   sprite.bounce_if_on_edge()      # back if on edge
#   time.sleep_ms(1000)             # delay 1s
