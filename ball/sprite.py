from processing import *


class Sprite:
  def __init__(self, x, y, w, h, i):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.image = i
  

  def draw(self):
    image(self.image, self.x, self.y, self.w, self.h)


  def move(self, xs, ys):
    self.x += xs
    self.y += ys



  def collision(self, item):
    right = self.x < item.x + item.w
    left = self.x + self.w > item.x
    down = self.y < item.y + item.h
    up = self.y + self.h > item.y
    collided = right and left and down and up
    return collided
    
  def collision(x1, y1, w1, h1, x2, y2, w2, h2):
    right = x1 < x2 + w2
    left = x1 + w1 > x2
    down = y1 < y2 + h2
    up = y1 + h1 > y2
    collided = right and left and down and up
    return collided
