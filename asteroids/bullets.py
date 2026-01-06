from processing import *

class Bullet:
  def __init__(self, x, y, dir):
    self.x = x
    self.y = y
    self.h = 3
    self.w = 3
    self.dir = dir
    
  def drawbullet(self):
    rect(self.x, self.y, self.w, self.h)
    
  def movebullet(self):
    if self.dir == "up":
      self.y -= 10
    if self.dir == "right":
      self.x +=10
    if self.dir == "down":
      self.y += 10
    if self.dir == "left":
      self.x -= 10
      
  def collision(self, item):
    right = self.x < item.x + item.w
    left = self.x + self.w > item.x
    down = self.y < item.y + item.h
    up = self.y + self.h > item.y
    collided = right and left and down and up
    return collided
