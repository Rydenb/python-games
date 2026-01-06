from processing import *
import random
from spaceship import *
from asteroid import *
from bullets import *

letgo = True
timer = 0

def setup():
  global asteroid, spaceship, s, asteroidlist, spaceship_right, spaceship_down, spaceship_left, bulletlist, score
  size(500, 500)
  asteroid = loadImage("asteroid.png")
  spaceship = loadImage("spaceship.png")
  spaceship_right = loadImage("spaceship_right.png")
  spaceship_down = loadImage("spaceship_down.png")
  spaceship_left = loadImage("spaceship_left.png")
  s = Spaceship(250, 250)
  asteroidlist = []
  for i in range(5):
    #asteroidlist.append(Asteroid(random.randint(50, 450), random.randint(50, 450)))
    asteroidlist.append(Asteroid(100, 100))
  bulletlist = []
  score = 0

    
  
  
def draw():
  global timer, score
  background(0, 0, 0)
  fill(255,255, 255)
  timer += 1
  if timer > 120:
    asteroidlist.append(Asteroid(600, 600))
    timer = 0

  
  for a in asteroidlist:
    image(asteroid, a.x, a.y, a.w, a.h)
    a.x += a.xspeed
    a.y += a.yspeed
    if a.x>550:
      a.x = -50
    if a.x <-50:
      a.x = 550
    if a.y > 550:
      a.y = -50
    if a.y < -50:
      a.y = 550
    
    if s.collision(a):
      textSize(50)
      text("game over", 130, 250)
      exit()
      
      
  for b in bulletlist:
    remove = False
    b.drawbullet()
    b.movebullet()
    for a in asteroidlist:
      if b.collision(a):
        asteroidlist.remove(a)
        score += 50
        remove = True
    if b.x < 0 or b.x > 500:
      remove = True
    if b.y < 0 or b.y > 500:
      remove = True
    
    if remove == True:
      bulletlist.remove(b)
  
  if s.direction == "up":
    image(spaceship, s.x, s.y, s.w, s.h)
  elif s.direction == "down":
    image(spaceship_down, s.x, s.y, s.w, s.h)
  elif s.direction == "right":
    image(spaceship_right, s.x, s.y, s.w, s.h)
  elif s.direction == "left":
    image(spaceship_left, s.x, s.y, s.w, s.h)
    
  textSize(20)
  text(score, 15, 15)
  

  


  
  if keyPressed:
    global letgo
    if key == 'a':
      s.x -= 3
      s.direction = "left"
    if key == 'd':
      s.x += 3
      s.direction = "right"
    if key == 'w':
      s.y -= 3
      s.direction = "up"
    if key == 's':
      s.y += 3
      s.direction = "down"
    if key == " " and letgo == True:
      bulletlist.append(Bullet(s.x+10, s.y, s.direction))
      letgo = False
      
      
      
def keyReleased():
  global letgo
  letgo = True


run()
