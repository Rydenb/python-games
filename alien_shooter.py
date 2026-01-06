from processing import *
from random import *
import math

timer = 0
tx = 200
ty = 370
score = 0
speed = 2
spawn_time = 60


def collision(x1, y1, w1, h1, x2, y2, w2, h2):
  right = x1 < x2 + w2
  left = x1 + w1 > x2
  down = y1 < y2 + h2
  up = y1 + h1 > y2
  collided = right and left and down and up
  return collided



def angle_speed_to_components(angle_degrees, speed):
  xspeed = speed * cos(radians(angle_degrees))
  yspeed = -(speed * sin(radians(angle_degrees)))
  return (xspeed, yspeed)

def xytoangle(x1, y1, x2, y2):
  return math.degrees(math.atan2(y1 - y2, x2 - x1))


class Alien():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = 65
    self.h = 50
    self.angle = degrees(atan2(-420, 200-x))
    
    
  def draw(self):
    image(alien_img, self.x, self.y, self.w, self.h)
    
  def update(self):
    global score
    xspeed, yspeed = angle_speed_to_components(self.angle, speed)
    self.x += xspeed
    self.y += yspeed
  
    if self.y > 500 or self.x < 0 or self.x > 500:
        alienlist.remove(self)
        
    
  
    

class Bullet():
  def __init__(self, x, y, angle):
    self.x = x
    self.y = y
    self.w = 30
    self.h = 30
    self.angle = angle
    self.speed = 10
    
  def draw(self):
    image(bullet_image, self.x, self.y, self.w, self.h)
    
  def update(self):
    xspeed, yspeed = angle_speed_to_components(self.angle, self.speed)
    self.x += xspeed
    self.y += yspeed

    if self.y < 0 or self.y > 500 or self.x < 0 or self.x > 500:
        bullet_list.remove(self)
        
  def collision(self, item):
    right = self.x < item.x + item.w
    left = self.x + self.w > item.x
    down = self.y < item.y + item.h
    up = self.y + self.h > item.y
    collided = right and left and down and up
    return collided
    


def setup():
  global turret, alien_img, alienlist, bullet_image, bullet_list, score
  size(500, 500)
  turret = loadImage("SpaceTurret.png")
  alien_img = loadImage("alien.png")
  alienlist = []
  bullet_image = loadImage("bullet.png")
  bullet_list = []
  
  
  
def draw():
  global timer, score, speed, spawn_time
  background(0, 0, 0)
  image(turret, tx, ty, 115, 130)
  textSize(25)
  text("score: " + str(score), 50, 450)
  speed += 0.001
  spawn_time-=0.01
  for i in alienlist:
    i.draw()
    i.update()
    
    if collision(tx, ty, 115, 130, i.x, i.y, i.w, i.h):
      fill(255, 255, 255)
      textSize(50)
      text("Game Over", 100, 250)
      exit()
    
  for i in bullet_list:
    i.draw()
    i.update()
    
    for j in alienlist:
      if i.collision(j):
        alienlist.remove(j)
        score += 1
        if i in bullet_list:
          bullet_list.remove(i)
  
  
  
  timer += 1
  if timer >= spawn_time:
    alienlist.append(Alien(randint(100, 400), -50))
    timer = 0



def mousePressed():
  angle = xytoangle(tx+43, ty, mouseX, mouseY)
  bullet_list.append(Bullet(tx+43, ty, angle))
  

  
run()
