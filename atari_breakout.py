from processing import *
import random
import math

def weighted_choice(items, percentages):
    # Ensure that percentages sum to 100 (or 1.0 if normalized)
    if sum(percentages) != 100:
        raise ValueError("Percentages must sum to 100")
    
    # Convert percentages to actual weight values (out of 100)
    weights = [p / 100 for p in percentages]
    
    # Calculate the total weight (which should be 1.0)
    total_weight = 1.0
    
    # Generate a random float between 0 and total_weight (which is 1.0)
    rand_num = random.uniform(0, total_weight)
    
    # Iterate through the items and their weights to find the selected item
    cumulative_weight = 0
    for item, weight in zip(items, weights):
        cumulative_weight += weight
        if rand_num <= cumulative_weight:
            return item


def collision(x1, y1, w1, h1, x2, y2, w2, h2):
  right = x1 < x2 + w2
  left = x1 + w1 > x2
  down = y1 < y2 + h2
  up = y1 + h1 > y2
  collided = right and left and down and up
  return collided

class Sprite:
  def __init__(self, x, y, w, h, image):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.image = image
  

  def draw(self):
    image(self.image, self.x, self.y, self.w, self.h)


  def move(self, xs, ys):
    self.x += xs
    self.y += ys

  def collision(self, item):
    right = self.x < item.x + item.w
    left = self.x + self.w > item.x
    down = self.y < item.y + item.h
    up = self.y + self.h > item.y
    collided = right and left and down and up
    return collided


#powerups


#bigger platform: when you break block with "+" on it powerup will drop down and will add width to the platform if collected

#extra ball: when block with powerup is broken another ball will spawn where the block was broken

#heart: when you break block with heart and you catch powerup 1 floor touch will be taken away

powerups = ["none", "extra heart", "bigger platform", "extra ball"]
percentages = [85, 5, 5, 5]


class Ball(Sprite):
  def __init__(self, x, y):
    super().__init__(x,y,25, 25, None)
    self.directionY = 10
    self.directionX = 6
    self.angle = 75
    self.speed = 10
    
    
  def reflectx(self):
    xspeed = self.speed*math.cos(math.radians(self.angle))
    yspeed = self.speed*math.sin(math.radians(self.angle))
    xspeed = -xspeed
    self.angle = math.degrees(math.atan2(yspeed, xspeed))
    
  def reflecty(self):
    xspeed = self.speed*math.cos(math.radians(self.angle))
    yspeed = self.speed*math.sin(math.radians(self.angle))
    yspeed = -yspeed
    self.angle = math.degrees(math.atan2(yspeed, xspeed))
    
  def move(self):
    xspeed = self.speed*math.cos(math.radians(self.angle))
    yspeed = self.speed*math.sin(math.radians(self.angle))
    self.x += xspeed
    self.y+=yspeed
    
  def draw(self):
    fill(255)
    ellipse(self.x, self.y, self.w, self.h)
    
  def update(self):
    global touched_floor
    self.move()
    if self.y > 650:
      ball_list.remove(self)
      if len(ball_list) <=0:
        touched_floor -= 1
        ball_list.append(Ball(250, 250))
    if self.y < 0:
      self.reflecty()
      
    if self.x < 25:
      self.reflectx()
      self.x= 25
    if self.x > 725:
      self.reflectx()
      self.x = 725
    
    if collision(self.x, self.y, self.w, self.h, mouseX-platform_width/2, 550, platform_width, 25):
      self.y = 550 - self.h
      # self.reflecty()
      distance = (self.x+(self.w/2))-((mouseX-platform_width/2) +(platform_width/2))
      percentage = distance/(platform_width/2)
      self.angle = 50*percentage-90
      
      
    textSize(25)
    text("lives: " + str(touched_floor), 10,350)
      
  
  
class Powerup(Sprite):
  def __init__(self, x, y, powerup_name):
    super().__init__(x, y, 10, 10, None)
    self.powerup_name = powerup_name
    
  def update(self):
    global platform_width, touched_floor
    self.y += 10
    if collision(self.x, self. y, 10, 10,mouseX-platform_width/2, 550, platform_width, 25):
      if self.powerup_name == "bigger platform":
        platform_width+=20
        powerup_list.remove(self)
      if self.powerup_name == "extra ball":
        ball_list.append(Ball(mouseX-platform_width/2, 520))
        powerup_list.remove(self)
      if self.powerup_name == "extra heart":
        touched_floor+=1
        powerup_list.remove(self)
        
    
  def draw(self):
    
    if self.powerup_name == "bigger platform":
      fill(255, 0, 0)
      rect(self.x+16, self.y+3, 11, 3)
      rect(self.x+20, self.y, 3, 10)
    if self.powerup_name == "extra ball":
      fill(255, 0, 0)
      ellipse(self.x+20, self.y, 25, 25)
    if self.powerup_name == "extra heart":
      heart_x = self.x + self.w / 2  # Center of the brick
      heart_y = (self.y + self.h / 2)-4
      fill(255, 0, 0)
      draw_heart(heart_x, heart_y, 25) #size 10

        



class Brick(Sprite):
  touching_brick = False
  
  def __init__(self, x, y, r, g, b):
    super().__init__(x, y, 50, 10, None)
    self.r = r
    self.g = g
    self.b = b
    self.exists = True
    self.powerup = weighted_choice(powerups, percentages)

  def draw(self):
    if self.exists:
      fill(self.r, self.g, self.b)
      rect(self.x, self.y, self.w, self.h)
      if self.powerup == "extra ball":
        fill(255,255,255)
        ellipse(self.x+20, self.y, 10, 10)
      elif self.powerup == "bigger platform":
        fill(255, 255, 255)
        noStroke()
        rect(self.x+16, self.y+3, 11, 3)
        rect(self.x+20, self.y, 3, 10)
      elif self.powerup == "extra heart":
        fill(255, 255, 255)
        #draw heart here
        heart_x = self.x + self.w / 2  # Center of the brick
        heart_y = (self.y + self.h / 2)-4
        draw_heart(heart_x, heart_y, 10) #size 10

      for b in ball_list:
        if collision(b.x, b.y, b.w, b.h, self.x, self.y, self.w, self.h):
          Ball.reflecty(b)
          b.y += 10
          #self.exists = False
          bricks.remove(self)#FIX NEXT
          if self.powerup == "extra ball":
            new = Powerup(self.x, self.y, "extra ball")
            powerup_list.append(new)
          elif self.powerup == "bigger platform":
            new = Powerup(self.x, self.y, "bigger platform")
            powerup_list.append(new)
          elif self.powerup == "extra heart":
            new = Powerup(self.x, self.y, "extra heart")
            powerup_list.append(new)




    

def setup():
  global ball_list, platform_width, powerup_list, p, bx, by, directionY, directionX, touched_floor, powerups, percentages, bricks, b
  p = Powerup(250, 250, "bigger platform")
  fill(255, 255, 255)
  p.draw()
  size(750, 650)
  platform_width = 100
  touched_floor = 5 #lives
 
  ellipseMode(CORNER)
  
  bricks = []
  for y in range(10, 100, 12):
      for x in range(10, 705, 52):
        bricks.append(Brick(x, y, 255, 0, 0))


  powerup_list = []
  
  ball_list = []
  ball_list.append(Ball(100, 100))
  
def draw():
  global touching_brick
  background(0)
  if len(bricks) == 0:
    for y in range(10, 100, 12):
      for x in range(10, 705, 52):
        bricks.append(Brick(x, y, 255, 0, 0))  
  
  #paddle
  fill(255)
  rect(mouseX-platform_width/2, 550, platform_width, 25)
  
  
  
  for b in ball_list:
    b.draw()
    b.update()
  
  for br in bricks:
    br.draw()
  
  
  for p in powerup_list:
    p.draw()
    p.update()
  
  #print("in draw: " + str(touching_brick))
  # if touching_brick == True:
  #   directionY = -directionY
  #   #print("in draw")
    
  if touched_floor ==0:
    textSize(100)
    fill(255, 0, 0)
    text('Game Over', 125, 325)
    exit()
  

  

  
def draw_heart(x, y, size):
    """
    Draws a heart shape.

    Args:
        x: The x-coordinate of the center of the heart.
        y: The y-coordinate of the center of the heart.
        size: The size of the heart.
    """
    
    noStroke();
    beginShape();
    vertex(x, y);
    bezierVertex(x - size / 2, y - size / 2, x - size, y + size / 3, x, y + size);
    bezierVertex(x + size, y + size / 3, x + size / 2, y - size / 2, x, y);
    endShape(CLOSE);

run()
  
