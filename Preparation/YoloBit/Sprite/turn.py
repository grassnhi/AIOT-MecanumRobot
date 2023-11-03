from game import *
game.reset()
import time

if True:
  sprite = game.create_sprite(0, 0)
  sprite.turn(1, 90)    # turn right 90 degrees
#   sprite.turn(0, 90)  # turn left 90 degrees

while True:
  sprite.move_by(1)
  sprite.bounce_if_on_edge()
  time.sleep_ms(1000)
