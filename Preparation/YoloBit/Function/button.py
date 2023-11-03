from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1

import music


def on_button_a_pressed():
  global fish, sprite
  display.show(Image.YES)
  for count in range(2):
    music.play(['C4:1'], wait=True)
    music.play(['D4:1'], wait=True)
    music.play(['E4:1'], wait=True)
    music.play(['C4:1'], wait=True)

button_a.on_pressed = on_button_a_pressed


def on_button_b_pressed():
  global fish, sprite
  display.show(Image.NO)
  for count2 in range(2):
    music.play(['C4:1'], wait=True)
    music.play(['D4:1'], wait=True)
    music.play(['E4:1'], wait=True)
    music.play(['C4:1'], wait=True)

button_b.on_pressed = on_button_b_pressed


while True:
    pass
