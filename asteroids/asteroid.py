import random

class Asteroid:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = 100
    self.h = 100
    self.xspeed = random.uniform(-3, 3)
    self.yspeed = random.uniform(-3,3)
