from processing import *
import random
import math


def collision(x1, y1, w1, h1, x2, y2, w2, h2):
  right = x1 < x2 + w2
  left = x1 + w1 > x2
  down = y1 < y2 + h2
  up = y1 + h1 > y2
  collided = right and left and down and up
  return collided
  
  
  
def astc(angle_degrees, speed):
  xspeed = speed * cos(radians(angle_degrees))
  yspeed = -(speed * sin(radians(angle_degrees)))
  return (xspeed, yspeed)

def xytoangle(x1, y1, x2, y2):
  return math.degrees(math.atan2(y1 - y2, x2 - x1))
  
  
def square(s):
  beginShape(QUADS)
  vertex(-s, s, s)
  vertex(-s, -s, s)
  vertex(s, -s, s)
  vertex(s, s, s)
  endShape()
  


def setup():
  global PI, a, offset, num, rotate, mode, posX, direction, size, posY, m, vx, vy, posZ, score
  global enemyZ, enemyX, enemyY,ew1, eh1, ew2, eh2, playerZ
  size(640 ,640, P3D)
  noStroke()
  PI = 3.14
  a = 0
  offset = PI/24.0
  num = 2
  mode = 0
  posX = 0
  posY=0
  posZ = 0
  direction = ""
  size = 40
  m = 0
  vx, vy = 4, 4
  enemyZ = -500
  enemyX, enemyY = 250, 250
  ew1, eh1, ew2, eh2 = 150, 150, 150, 150
  score = 0
  playerZ = 300

  
  
  
def draw():
  global PI, a, offset, num, r, g, b, mode, posX, direction, size, posY, m, posZ
  global vx, vy, vz
  global enemyZ, enemyY, enemyX,ew1, eh1, ew2, eh2
  global score
  lights()
  background(0, 0, 100)
  
  fill(0, 0, 0)
  pushMatrix()
  translate(0, 0, enemyZ)
  if enemyZ < playerZ:
    if mode == 0:
      rect(posX - size / 2, posY - size / 2, size * 1.25, size * 1.25)
    else:
      ellipse(posX, posY, size * 1.25, size * 1.25)
  popMatrix()
  
  
  pushMatrix()
  angle = xytoangle(posX, posY, mouseX, mouseY)
  vx, vy = astc(angle, 10)[0], astc(angle, 10)[1]
  translate(posX, posY, playerZ)
  
  
  if posZ < 1000:
    posZ+=10
  else:
    posZ=100
  posY+= vy
  if mouseX > posX-size/2 and mouseX < posX + size/2 and mouseY > posY-size/2 and mouseY < posY + size/2:
    vx = 0
    vy = 0
  else:
    posX+=vx
    posY+=vy  
  for i in range(num):
    fill(50*i, 0, 20*i)
    gray = map(i, 0, num-1, 0, 255)
    pushMatrix()
    rotateY(a/2+offset*i)
    rotateX(a+offset*i)

    if mode == 0:
      box(size)
    if mode  == 1:
      sphere(size)
    popMatrix()
  a+=0.01
  
  popMatrix()
  
  #top wall
  pushMatrix()
  
  fill(0, 255, 0)
  
  translate(0, 0, enemyZ)
  
    
  rect(enemyX, enemyY, ew1, eh1 / 4)

  popMatrix()
  
  
  #left wall
  pushMatrix()
  
  fill(255, 0, 0)
  
  translate(0, 0, enemyZ)
  

  rect(enemyX, enemyY, ew1 /4 , eh1)

  popMatrix()
  
  #bottom wall
  pushMatrix()
  
  
  fill(0, 0, 255)
  
  translate(0, 0, enemyZ)
  
    
  rect(enemyX, enemyY + (3 / 4) * eh1, ew1, eh1 / 4)

  popMatrix()
  
  
  #right wall
  pushMatrix()
  
  
  fill(123, 0, 123)
  
  translate(0, 0, enemyZ)
    
    
  rect(enemyX + (3/4)  * ew1, enemyY, ew1/4, eh1)

  popMatrix()
  
  
  if enemyZ < 1500:
    enemyZ+=random.randint(7, 15)
    
  if enemyZ > 1500:
    enemyZ = -500
    eh1 = random.randint(200, 600)
    ew1 = random.randint(200, 600)
    enemyX = random.randint(0, 300)
    enemyY = random.randint(0, 300)
  
  if mode == 0:
    shadowX= posX - size / 2
    shadowY = posY - size / 2
  
  else:
    shadowX = posx
    shadowY = posY
  
  dead = (
    collision(shadowX, shadowY, size, size, enemyX, enemyY, ew1, eh1 / 4) or
    collision(shadowX, shadowY, size, size, enemyX, enemyY, ew1 /4, eh1) or
    collision(shadowX, shadowY, size, size, enemyX, enemyY + (3 / 4) * eh1, ew1, eh1 / 4) or
    collision(shadowX, shadowY, size, size, enemyX + (3/4)  * ew1, enemyY, ew1/4, eh1)
    )
  if abs(enemyZ - playerZ) <=5:
    if dead:
      textSize(60)
      fill(200, 0, 0)
      textAlign(CENTER, CENTER)
      text("Game over", width/2, height/2)
      exit()
    else:
      score+=1

  textSize(32)
  fill(150, 0, 150)
  text("score : " + str(score), 100, 100)


def keyPressed():
  global direction
  if key == "d":
      direction = "right" 
  if key == "a":
    direction = "left"
  if key == "w":
    direction = "up"
  if key == "s":
    direction = "down"
    
    
def keyReleased():
  global mode, posX, posY, direction
  direction = "idle"
  if key == " ":
    mode = not mode
  if key == "z":
    posX = -250
    posY=10
    direction = ""
  if key == "t":
    direction = "shrink"
  if key == 'g':
    direction = "grow"
  if key == "e":
    direction = "forward"
  if key == 'q':
    direction = "arch"
    
  
run()