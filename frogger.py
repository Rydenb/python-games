from processing import *

def check_gameover():
  global lives, fx, fy
  if lives == 1:
    fill(255, 0, 0)
    textSize(75)
    text("gameover", 50, 250)
    exit()
    fill(255, 255, 255)
  else:
    lives -= 1
    fx = 260
    fy = 470
    
def check_lilypad():
  global pad1, pad2, pad3, pad4, pad5, fx, fy
  #1 : 0-90
    #2 : 91-194
    #3 : 195 - 304
    #4 : 305 - 407
    #5 : 408 - 500
  if fx >= 0 and fx <= 90 and fy < 50:
    pad1 = True
    fx = 260
    fy = 470
  elif fx >= 91 and fx <= 194 and fy < 50:
    pad2 = True
    fx = 260
    fy = 470
  elif fx >= 195 and fx <= 304 and fy < 50:
    pad3 = True
    fx = 260
    fy = 470
  elif fx >= 305 and fx <= 407 and fy < 50:
    pad4 = True
    fx = 260
    fy = 470
  elif fx >= 408 and fx <= 500 and fy < 50:
    pad5 = True
    fx = 260
    fy = 470
  
  
  if pad1 and pad2 and pad3 and pad4 and pad5:
    textSize(75)
    text("You Win!", 100, 250)
    exit()
    


def collision(x1, y1, w1, h1, x2, y2, w2, h2):
  right = x1 < x2 + w2
  left = x1 + w1 > x2
  down = y1 < y2 + h2
  up = y1 + h1 > y2
  collided = right and left and down and up
  return collided

class Car:
  def __init__(self, x, y, w, h, velocity, image):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.velocity = velocity
    self.image = image
    
  def draw(self):
    image(self.image, self.x, self.y, self.w, self.h)
    
    
class Log:
  def __init__(self, x, y, w, velocity, image):
    #small log is slow big log is fast
    self.x = x
    self.y = y
    self.w = w
    self.h = 30
    self.velocity = velocity
    self.image = image
    
  def draw(self):
    image(self.image, self.x, self.y, self.w, self.h)
    
class Lilypad:
  def __init__(self, x):
    #lilypad coordintates
    #1 : 0-90
    #2 : 91-194
    #3 : 195 - 304
    #4 : 305 - 407
    #5 : 408 - 500
    self.x = x
    self.w = 1

def setup():
  global frog, car_list, turtles, log_image, bg, fx, fy, small_log, log_list, lives, pad1, pad2, pad3, pad4, pad5
  size(500, 500)
  frog = loadImage("frog.png")
  car4_img = loadImage("cars.png")
  car2_img = loadImage("cars2.png")
  car3_img = loadImage("cars3.png")
  car1_img = loadImage("cars4.png")
  car5_img = loadImage("cars5.png")
  turtles = loadImage("turtles.png")
  log_image = loadImage("log.png")
  small_log = loadImage("small_log.png")
  bg = loadImage("frogger_background.png")
  fx = 230
  fy = 470
  lives = 3
  pad1 = False
  pad2 = False
  pad3 = False
  pad4 = False
  pad5 = False

  log_list = [Log(250, 210, 200, 2, log_image),
  Log(230, 170, 100, -2, log_image),
  Log(70, 170, 100, -2, log_image),
  Log(390, 170, 100, -2, log_image),
  Log(280, 130, 180, 2, log_image),
  Log(540, 130, 180, 2, log_image),
  Log(70, 90, 180, -2, log_image),
  Log(70, 60, 100, 2, log_image),
  Log(230, 60, 100, 2, log_image),
  Log(390, 60, 100, 2, log_image)
    ]
  
  car_list = [Car(250, 430, 40, 30, -1, car1_img),
              Car(250+150, 430, 40, 30, -1, car1_img),
              Car(250 + 300, 430, 40, 30, -1, car1_img),
               Car(250, 390, 40, 30, 1.1, car2_img),
                Car(250+150, 390, 40, 30, 1.1, car2_img),
                 Car(250+150, 390, 40, 30, 1.1, car2_img),
               Car(250, 355, 40, 30, -1.4, car3_img),
               Car(250+150, 355, 40, 30, -1.4, car3_img),
               Car(250+300, 355, 40, 30, -1.4, car3_img),
             Car(250, 320, 40, 30, 1.1, car4_img),
              Car(250+150, 320, 40, 30, 1.1, car4_img),
               Car(250+300, 320, 40, 30, 1.1, car4_img),
             Car(250, 285, 75, 30, -1.4, car5_img),
             Car(250+150, 285, 70, 30, -1.4, car5_img)
             ]

  

  


def draw():
  global frog, car1, car2, car3, car4, car5, turtles, log, bg, fx, fy, car5x, car5y, car4x, car4y, car3x, car3y, car2x, car2y, car1y, car1x, velocity1, velocity2, velocity3
  background(0, 0, 0)
  image(bg, 0, 0, 500, 500)
  textSize(30)
  text("lives:"+str(lives), 10, 500)
  check_lilypad()
  
  if pad1 == True:
    image(frog, 20, 30, 30, 30)
  if pad2 == True:
    image(frog, 130, 30, 30, 30)
  if pad3 == True:
    image(frog, 240, 30, 30, 30)
  if pad4 == True:
    image(frog, 345, 30, 30, 30)
  if pad5 == True:
    image(frog, 450, 30, 30, 30)
    
  
  for l in log_list:
    l.draw()
    l.x += l.velocity
    if l.velocity < 0:
      if l.x < -250:
        l.x = 575
    elif l.velocity > 0:
      if l.x >550:
        l.x = -250
        
  image(frog, fx, fy, 30, 30)
  
  for c in car_list:
    c.draw()
    c.x += c.velocity
    if c.velocity < 0:
      if c.x < -80:
        c.x = 550
    elif c.velocity > 0:
      if c.x >550:
        c.x = -50
        
  
        
    
    
    if collision(fx, fy, 30, 30, c.x, c.y, c.w, c.h):
      check_gameover()
      
      
  
  touching_water = False
  if fy > 50 and fy < 245:
    touching_water = True
    
  for l in log_list:
    if collision(fx, fy, 30, 30, l.x, l.y, l.w, l.h):
      touching_water = False
      fx += l.velocity
      fy = l.y
    
    
  if touching_water == True:
    check_gameover()
    
      
  
  # image(car5, car5x, car5y, 75, 35)
  # image(car5, car5x+200, car5y, 75, 35)
  # image(car4, car4x, car4y, 50, 40)
  # image(car4, car4x-200, car4y, 50, 40)
  # image(car4, car4x-400, car4y, 50, 40)
  # image(car3, car3x, car3y, 50, 40)
  # image(car3, car3x+200, car3y, 50, 40)
  # image(car3, car3x+400, car3y, 50, 40)
  # image(car2, car2x, car2y, 50, 40)
  # image(car2, car2x-200, car2y, 50, 40)
  # image(car2, car2x-400, car2y, 50, 40)
  # image(car1, car1x, car1y, 40, 40)
  # image(car1, car1x+200, car1y, 40, 40)
  # image(car1, car1x+400, car1y, 40, 40)
  
    
def keyPressed():
  global fy, fx
  if key == CODED:
    if keyCode == UP:
      fy -= 37
    if keyCode == DOWN:
      fy +=37
    if keyCode == RIGHT:
      fx += 40
    if keyCode == LEFT:
      fx -= 40
  

run()
