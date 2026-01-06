from processing import *
from random import *

circles = 0

class Circle:
  def __init__(self, x, y, size, color, xv, yv):
    self.x = x
    self.y = y
    self.size = size
    self.color = color
    self.xv = xv
    self.yv = yv
    
  def update(self):
    self.draw()
    self.move()
    if self.x + self.size/2 > 500 or self.x - self.size/2 < 0:
      self.xv *= -1
    elif self.y - self.size/2 < 0 or self.y + self.size/2 > 500:
      self.yv *= -1
    
  def move(self):
    self.x += self.xv
    self.y += self.yv
    
  def draw(self):
    fill(self.color[0], self.color[1], self.color[2])
    ellipse(self.x, self.y, self.size, self.size)
    

clist = []
def mouseClicked():
  global circles
  if circles < 300:
    clist.append(Circle(mouseX, 
                        mouseY, 
                        randint(50, 200), 
                        (randint(1, 255), randint(1, 255), randint(1, 255)), 
                        choice([randint(-5, -1), randint(1, 5)]),
                        choice([randint(-5, -1), randint(1, 5)])
                        ))
    circles += 1


def setup():
  size(500, 500)

def draw():
  background(255, 255, 255)
  for c in clist:
    c.update()
    
  textSize(25)
  fill(0, 0, 0)
  text("circles: " + str(circles), 25, 25)


run()
