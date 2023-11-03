import music

def playsong():
  for count in range(2):
    music.play(['C4:1'], wait=True)
    music.play(['D4:1'], wait=True)
    music.play(['E4:1'], wait=True)
    music.play(['C4:1'], wait=True)
  for count2 in range(2):
    music.play(['E4:1'], wait=True)
    music.play(['F4:1'], wait=True)
    music.play(['G4:1'], wait=True)

if True:
  playsong()

while True:
    pass
