from game import *
game.reset()
import time

if True:
  sprite = game.create_sprite(2, 2)

while True:
  sprite.move_by(1)
  time.sleep_ms(1000)
