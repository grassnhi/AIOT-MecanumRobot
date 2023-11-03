from game import *
game.reset()
import time

if True:
  sprite = game.create_sprite(2, 2)

while True:
  sprite.move_by(1)
  sprite.bounce_if_on_edge()
  time.sleep_ms(1000)
