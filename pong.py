from random import *
from processing import *
import random

plx = 100
ply = 100
x = 400
y = 300
prx = 700
pry = 150
pl_score = 0
pr_score = 0
direction = 5
direction2 = 4
HasPassed = False
timer = 0
random1 = random.randint(4,9)
random2 = random.randint(4,9)


def display_score():
  #scoring
  fill(0, 255, 0)
  textSize(40)
  text(pl_score, 20, 50)
  fill(0, 255, 0)
  textSize(40)
  text(pr_score, width-40, 50)


def display_paddles():
  global pry, prx, ply, plx
  #makes paddles
  fill(234, 212, 123)
  rect(plx, ply, 20,100, 10)
  fill(234, 212, 123)
  rect(prx, pry, 20,100, 10)
  #code for AI paddle
  if y > pry:
    pry += random1
  elif y < pry:
      pry -= random2

def display_ball():
  #makes ball
  global x, y, direction, direction2, plx, ply, prx, pry, pr_score, pl_score, timer
  fill(255, 255, 255)
  ellipse(x, y, 50, 50)

  if timer > 100:
    y += direction
    x += direction2
  #wall detection
  if y > 600:
    direction = -direction
  if y < 50:
    direction = -direction
    y += direction
    #puts ball back in the middle after someone scores
  if x < 50:
    x = 400
    y = 300
    pl_score += 1
    timer = 0
    direction = 5
    direction2 = 4
  if x > 790:
    x = 400
    y = 300
    pr_score += 1
    timer = 0
    direction = 5
    direction2 = 4
  #paddle detection
  if x >prx -35 and y > pry-60 and y < pry+60:
    direction2 = -direction2*1.1
  if x < plx + 35 and y > ply-60 and y < ply+60:
    direction2 = -direction2*1.1
  
  

def setup():
  size(800, 600)

def draw():
  global timer
  timer += 1
  
  background(0, 0, 0)
  display_paddles()
  display_ball()
  display_score()
  
  
def keyPressed():
  global ply, pry
  if key == "w" or key == "W":
    ply -= 10
  if key == "s" or key == "S":
    ply += 10
  if key == CODED:
    if keyCode == UP:
      pry -= 10
    if keyCode == DOWN:
      pry += 10



run()



