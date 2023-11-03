# from game import *
# game.reset()
# import time

# if True:
#   sprite = game.create_sprite(0, 0)

# while True:
#   sprite.move_by(1)
#   time.sleep_ms(1000)
#   sprite.move_by(1)
#   time.sleep_ms(1000)
#   sprite.move_by(1)
#   time.sleep_ms(1000)
#   sprite.move_by(1)
#   time.sleep_ms(1000)

##### LOOP 4 times #####
from game import *
game.reset()

import time


sprite = game.create_sprite(0, 0)
for count in range(4):
  sprite.move_by(1)
  time.sleep_ms(1000)
