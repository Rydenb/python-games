from processing import *
import math
import random
import time

def collision(x1, y1, w1, h1, x2, y2, w2, h2):
  right = x1 < x2 + w2
  left = x1 + w1 > x2
  down = y1 < y2 + h2
  up = y1 + h1 > y2
  collided = right and left and down and up
  return collided

class Bacteria:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = 60
    self.h = 60
    self.timer = 0
    self.nextx = random.randint(1, 500)
    self.nexty = random.randint(1, 500)
    
  def glide(self, target_x, target_y, speed):
    distance_x = target_x - self.x
    distance_y = target_y - self.y
    total_distance = math.hypot(distance_x, distance_y)

    if total_distance <= speed:
        self.x = target_x
        self.y = target_y
        return True
    else:
        self.x += (distance_x / total_distance) * speed
        self.y += (distance_y / total_distance) * speed
        return False
    
  def update(self):
    self.timer +=1
    if self.timer == 120:
      if len(bacteria_list) < 300:
        bacteria_list.append(Bacteria(self.x, self.y))
      self.timer = 0
    
    res = self.glide(self.nextx, self.nexty, 1.5)
    if res == True:
      self.nextx = random.randint(1, 500)
      self.nexty = random.randint(1,500)
    
  def draw(self):
    image(bacteria, self.x, self.y, self.w,self.h)
    
class sanitizer:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = 50
    self.h = 100
    
  def draw(self):
    image(sanitizer, self.x, self.y, self.w, self.h)
  
    
    
class Waterdrop:
  def __init__(self, x, y):
    self.x = s.x
    self.y = s.y
    self.w = 25
    self.h = 40
    self.timer = 0
    
  def draw(self):
    image(waterdrop, self.x, self.y, self.w, self.h)
    
  def update(self):
    self.timer += 1
    self.y+=3
    if self.timer == 120:
      droplets.remove(self)

def setup():
  global bacteria, b, bacteria_list, sanitizer, s, start_time, waterdrop, w, droplets
  s = sanitizer(250, 250)
  w = Waterdrop(100, 100)
  size(500, 500)
  bacteria = loadImage("bacteria.png")
  sanitizer = loadImage("hand_sanitizer.png")
  waterdrop = loadImage("waterdrop.png")
  bacteria_list = []
  bacteria_list.append(Bacteria(100, 100))
  bacteria_list.append(Bacteria(150, 150))
  bacteria_list.append(Bacteria(170, 170))
  bacteria_list.append(Bacteria(190, 190))
  start_time = time.time()
  droplets = []
  droplets.append(Waterdrop(100, 100))
  
  
def mouseClicked():
  if len(droplets) < 10 and frameCount > 180:
    droplets.append(Waterdrop(25, 25))

def draw():
  background(176, 213, 230)
  s.x = mouseX-22
  s.y = mouseY-50
  
  for i in bacteria_list:
    i.draw()
    i.update()
    for d in droplets:
      if collision(i.x,i.y, i.w, i.h, d.x, d.y, d.w,d.h):
        if i in bacteria_list:
            bacteria_list.remove(i)
          
  for d in droplets:
    d.draw()
    d.update()
    
  
  s.draw()
  
  
  



run()
