from game import *
game.reset()

import time


sprite = game.create_sprite(0, 0)

for count2 in range(4):
    for count in range(4):
        sprite.move_by(1)
        time.sleep_ms(1000)
    sprite.turn(1, 90)
