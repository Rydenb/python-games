from turtle import *
import random


speed(0)
tracer(100)

def square():
  for i in range(4):
    color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    forward(100)
    right(90)
    

def triangle():
  for i in range(3):
    color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    forward(100)
    right(120)
    left(10)

for i in range(10080):
  left(10)
  square()
  circle(100)
  left(1)
  

