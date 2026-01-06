from processing import *
from random import *

def collision(x1, y1, w1, h1, x2, y2, w2, h2):
  right = x1 < x2 + w2
  left = x1 + w1 > x2
  down = y1 < y2 + h2
  up = y1 + h1 > y2
  collided = right and left and down and up
  return collided


class Player:
  def __init__(self, x, y, image):
    self.x = x
    self.y = y
    self.w = 60
    self.h = 60
    self.yspeed = 9
    self.image = image
    self.direction = "right"
    self.cooldown = 0
    
  def draw(self):
    image(self.image, self.x, self.y, self.w,self.h)
    
  def player_fall(self):
    self.y += self.yspeed
    self.yspeed += 0.25
    
    
class Monster:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = 100
    self.h = 65
    self.direction = "right"
    self.xspeed = 10
    
  def draw(self):
    image(monster, self.x, self.y, self.w,self.h)
    
  def update(self):
    if self.direction == "right" and self.x < width-100:
      self.x += self.xspeed
    if self.direction == "right" and self.x >= width-100:
      self.direction = "left"
    if self.direction == "left" and self.x > 0:
      self.x -= self.xspeed
    if self.direction == "left" and self.x <= 0:
      self.direction = "right"
      
    if p.y < 100:
      self.y += 5
      
    if self.y > 500:
      self.y = -6000
      
  
    
class Platforms:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = 65
    self.h = 10
    
  def draw(self):
    fill(121, 189, 40)
    rect(self.x, self.y, self.w, self.h, 20 ,20, 20, 20)
    
  def move_down(self):
    self.y += 5
    
class Breaking_platform(Platforms):
  def __init__(self, x, y):
    super().__init__(x, y)
    self.broken = False
    
  def draw(self):
    fill(139, 69, 39)
    rect(self.x, self.y, self.w, self.h, 20 ,20, 20, 20)
  
  def move_down(self):
    self.y += 5
    
class Bullet():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = 15
    self.h = 15
    self.image = bullet_image
    
  def draw(self):
    image(self.image, self.x, self.y, self.w, self.h)
    
  def update(self):
    self.y -= 20
  
  

def setup():
  global bullets, bullet_image, b, left_doodle, right_doodle, p, pl, platforms,score, monster, m, bp, breaking_platforms, shooting_doodle
  size(500, 500)
  score = 0
  right_doodle = loadImage("right.png")
  left_doodle = loadImage("left.png")
  shooting_doodle = loadImage("shoot.png")
  flipped_doodle = loadImage("flipped_doodle.png")
  monster = loadImage("image-removebg-preview.png")
  bullet_image = loadImage("doodle_bullet.png")
  p = Player(100, 200, right_doodle)
  m = Monster(100, 10)
  bullets = [
    
    ]
  platforms = [
    Platforms(randint(0, 100), randint(100, 150)),
    Platforms(randint(50, 150), randint(150, 350)),
    Platforms(randint(150, 400), randint(0, 400)),
    Platforms(randint(200, 400), randint(0, 100)),
    Platforms(randint(350, 400), randint(-200, 0)),
    Platforms(randint(0, 400), randint(-200, 0)),
    Platforms(100, 400)
    ]
  breaking_platforms = [
    Breaking_platform(randint(300, 400), randint(200, 350)),
    Breaking_platform(randint(100, 400), randint(300, 400)),
    Breaking_platform(randint(150, 400), randint(0, 400))
    ]


def draw():
  global score, m 
  background(255, 255, 255)
  p.draw()
  m.draw()
  m.update()
  p.player_fall()
  fill(0, 0, 0)
  textSize(30)
  text(score, 20, 30)
  #image(monster, 100, 100, 100, 75)
  for b in bullets:
    b.draw()
    b.update()
    if b.y < -50:
      bullets.remove(b)
    if collision(m.x, m.y, 100, 65, b.x, b.y, b.w, b.h):
      m.y -= 6000
  for i in platforms:
    i.draw()
    if collision(p.x, p.y, p.w, p.h, i.x, i.y, i.w, i.h) and p.yspeed > 0:
      p.yspeed = -9
    
    if p.y < 100:
      i.move_down()
      score += 1
      
    if i.y > height:
      # print(i.y)
      i.y = 0
      i.x = randint(1, 500)
  
  if p.cooldown > 0:
    p.cooldown -= 1

  if p.y > height:
    exit()
    textSize(75)
    fill(255, 0, 0)
    text("Game Over", 50, 250)
      
  # p.image = right_doodle
  if p.direction == "right":
    p.image = right_doodle
  if p.direction == "left":
    p.image = left_doodle
  if keyPressed:
    if key == CODED:
      if keyCode == RIGHT:
        p.x += 5
        p.direction = "right"
      if keyCode == LEFT:
        p.x -= 5
        p.direction = "left"
      if keyCode == UP and p.cooldown == 0:
        p.image = shooting_doodle
        bullets.append(Bullet(p.x+20, p.y))
        p.cooldown = 10
        
        
  for i in breaking_platforms:
      i.draw()
      if collision(p.x, p.y, p.w, p.h, i.x, i.y, i.w, i.h) and p.yspeed > 0:
        i.broken = True
        
      
      if p.y < 100:
        i.move_down()
        score += 1
        
      if i.y > height and not i.broken:
        # print(i.y)
        i.y = 0
        i.x = randint(1, 500)
        
      if i.broken:
        i.y += 9
      if i.y > 500:
        i.y = -100
        i.x = randint(150, 400)
        i.broken = False
      
        
  if collision(p.x, p.y, p.w, p.h, m.x, m.y, m.w, m.h):
    textSize(75)
    fill(255, 0, 0)
    text("Game Over", 50, 250)
    exit()
    
  
run()
