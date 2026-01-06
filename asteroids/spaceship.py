class Spaceship:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = 25
    self.h = 25
    self.direction = "up"
    
  def collision(self, item):
    right = self.x < item.x + item.w
    left = self.x + self.w > item.x
    down = self.y < item.y + item.h
    up = self.y + self.h > item.y
    collided = right and left and down and up
    return collided
