from processing import *

def draw():
  global cookie
  size(500, 500)
  image(cookie, 120, 120, 250, 250)
  fill(0, 0, 0)
  textSize(100)
  text(str(clicker), 25, 100)


  
def setup():
  global cookie
  global clicker
  clicker = 0
  cookie = loadImage("PerfectCookie (1).png")
  
def mouseClicked():
  global clicker
  if mouseX > 127 and mouseX < 363 and mouseY < 359 and mouseY > 126:
    clicker +=1
    

  
  
run()
