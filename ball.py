from processing import *
from sprite import *


class Ball(Sprite):
  def __init__(self):
    super().__init__(250, 250, 100, 100, ball)
    self.xspeed = 2
    self.yspeed = 2



def setup():
  global s, ball
  size(500, 500)
  ball = loadImage("ball.png")
  s = Ball()
  
  
def draw():
  global xspeed
  background(100)
  s.draw()
  
  
  s.y += s.yspeed
  s.yspeed += 0.1
  if s.y > 400:
    s.yspeed = s.yspeed*-1
    s.yspeed += 0.5
    s.y = 400
  
    
  
  
  s.x += s.xspeed
  if s.x > 400:
    s.xspeed = -2
  if s.x < 1:
    s.xspeed = 2
    
def keyPressed():
  if key == " "and s.y > 375:
    s.yspeed = -5
  
run()
