from processing import *
from random import *

strawberries = []
apples = []
rasberries = []

frames = 0

def setup():
  global strawberry, apple, score, rasberry
  size(425, 525)
  strawberry = loadImage("strawberry-removebg-preview.png")
  apple = loadImage("apple.png")
  rasberry = loadImage("Rasberry.png")
  score = 0

def points():
  global score
  textSize(15)
  fill(255, 255, 255)
  text("score:" + str(score), 175, 50)

def draw():
  global frames, score
  background(25, 31, 71)
  frames += 1
  points()
  
  
  
  if frames == 17:
    strawberries.append([0, randint(0, height)])
    apples.append([randint(0, width), 0])
    rasberries.append([width, randint(0, height)])
    frames = 0
  
  for a in apples:
    image(apple, a[0], a[1], 50, 50)
    a[1] += 3
    touch = dist(a[0], a[1], mouseX, mouseY)
    if touch < 45:
      apples.remove(a)
      score +=1
  
  for s in strawberries:
    image(strawberry, s[0], s[1],50, 50)
    s[0] += 3
    
    touch = dist(s[0], s[1], mouseX, mouseY)
  
    if touch < 45:
      strawberries.remove(s)
      score += 1
    
  for r in rasberries:
    image(rasberry, r[0], r[1], 50, 50)
    r[0] -= 3
    touch = dist(r[0], r[1], mouseX, mouseY)
    if touch < 45:
      rasberries.remove(r)
      score += 1
  
    


    
    
    
    
run()
  
