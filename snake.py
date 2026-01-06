from processing import *
from random import *

def scene():
  c = [200, 30, 50]
  fill(c[0], c[1], c[2])
  y=0
  while y < height:
    x = 0
    while x < width:
      if(x == 0 or x == (width-dim-dim) or y == 0 or y == (height-dim-dim)):
        fill(c[0], c[1], c[2])
      rect(x,y,dim,dim)
      x +=dim
    y +=dim
    c[0] += 5
    c[1] += 7
    c[2] += 10
    
    
def setup():
  global points
  points = 0
  global sx, sy
  global dim
  global direction
  global body
  size(500, 500)
  direction = ''
  dim = 25
  sx = width/2
  sy = height/2
  frameRate(30)
  apple_spawn()
  body = []
  body.append((sx, sy))

def apple_display():
  global ax, ay
  fill(0, 255, 0)
  rect(ax,ay,dim,dim)

def snake():
  fill(0, 0, 255)
  rect(sx, sy, dim, dim)
    
  for coordinates in body:
    if body.index(coordinates) == len(body)-1:
      fill(0, 0, 128)
    else:
      fill(0, 0, 255)
    rect(coordinates[0], coordinates[1], dim, dim)
    
  
def snake_move():
  global sx
  global sy
  if direction == 'right':
    sx += dim
  if direction == 'left':
    sx -= dim
  if direction == 'up':
    sy -= dim
  if direction == 'down':
    sy += dim
  
  
def keyPressed():
  global direction
  if key == CODED:
    if keyCode == RIGHT and keyCode == DOWN:
      print("hello")
      if direction == 'right':
        direction = 'down'
      else:
        direction = 'right'
    
    if keyCode == RIGHT and direction != 'left':
      direction = 'right'
    if keyCode == LEFT and direction != 'right' :
      direction = 'left'
    if keyCode == UP and direction != 'down' :
      direction = 'up'
    if keyCode == DOWN and direction != 'up':
      direction = 'down'
  
def GameOver():
  textSize(50)
  fill(100, 100, 199)
  if(sx < 0 or sx > width or sy > height or sy < 0) or len(body) > 1 and body[0] in body[2::]:
    text('Game Over', 115, 250)
    exit()

def draw():
  global points
  scene()
  snake()
  snake_move()
  body.append((sx, sy))
  if(sx == ax and sy == ay):
    body.append((sx, sy))
    apple_spawn()
    points += 1
  body.pop(0)
  apple_display()
  display_points()
  GameOver()
  
def apple_spawn():
  global ax, ay
  ax = randint(1, (width-dim)/dim)*25
  ay = randint(1, (height-dim)/dim)*25
  
def display_points():
  fill(255, 255, 255)
  textSize(30)
  text(points, dim*1, dim*2)
  

  

run()
