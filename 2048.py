from processing import *
import random

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



def setup():
  global grid
  size(500, 500)
  grid = [[0, 0, 0, 0], [0, 256, 0, 0], [2, 2, 0, 8], [0, 2, 2, 0]]
  
  
  
def move_grid(dir):
  if dir == "up":
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        k = i
        while k > 0 and grid[k][j] != 0:
          if grid[k-1][j] == 0:
            grid[k-1][j]=grid[k][j]
            grid[k][j]=0
          elif grid[k-1][j] == grid[k][j]:
            grid[k-1][j] = grid[k][j]*2
            grid[k][j] = 0
          k-=1
  elif dir == "down":
    for i in range(len(grid)-1, -1, -1):
      for j in range(len(grid[i])):
        k = i
        while k < 3 and grid[k][j] != 0:
          if grid[k+1][j] == 0:
            grid[k+1][j]=grid[k][j]
            grid[k][j]=0
          elif grid[k+1][j] == grid[k][j]:
            grid[k+1][j] = grid[k][j]*2
            grid[k][j] = 0
          k+=1
  elif dir == "right":
    for i in range(len(grid)):
      for j in range(len(grid[i])-1, -1, -1):
        k = j
        while k < 3 and grid[i][k] != 0:
          if grid[i][k+1] == 0:
            grid[i][k+1]=grid[i][k]
            grid[i][k]=0
          elif grid[i][k+1] == grid[i][k]:
            grid[i][k+1] = grid[i][k]*2
            grid[i][k] = 0
          k+=1
          
          
  elif dir == "left":
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        k = j
        while k > 0 and grid[i][k] != 0:
          if grid[i][k-1] == 0:
            grid[i][k-1]=grid[i][k]
            grid[i][k]=0
          elif grid[i][k-1] == grid[i][k]:
            grid[i][k-1] = grid[i][k]*2
            grid[i][k] = 0
          k-=1
          


          
def spawn_number():
  randomx = random.randint(0,3)
  randomy = random.randint(0,3)
  while grid[randomy][randomx] != 0:
    randomx = random.randint(0,3)
    randomy = random.randint(0,3)
  
  randomnum = weighted_choice([2,4], [90, 10])
  grid[randomy][randomx] = randomnum
    
  
def draw_grid():
  x = 100
  y = 100
  
  
  textSize(100)
  fill(255, 222, 173)
  rect(100, 25, 400, 400, 7)
  for i in grid:
    for j in i:
      fill(255, 235, 205)
      rect(x, y-72, 95, 95, 7)
      fill(0, 0, 0)
      if j != 0:
        textSize(50)
        if j > 1000:
          textSize(30)
          text(j, x+15, y-10)
        elif j > 100:
          text(j, x+4.4, y)
        elif j < 100:
          text(j, x+30, y)
        
        
          
      x += 100
    y +=100
    x = 100
  
  
def draw():
  global grid
  background(255, 255, 255)
  draw_grid()
  
def keyPressed():
  if keyCode == UP:
    move_grid("up")
    spawn_number()
  if keyCode == DOWN:
    move_grid("down")
    spawn_number()
  if keyCode == RIGHT:
    move_grid("right")
    spawn_number()
  if keyCode == LEFT:
    move_grid("left")
    spawn_number()
  
  

  
run()
