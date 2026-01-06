import random

active = True

high = int(input("choose the maximum number"))
low = int(input("choose the minimum number"))

number = int(input("choose a number for the computer to guess"))



computer_guesses = 0

while active == True:
  #computer_guess = random.randint(low, high)
  computer_guess = (low + high)//2
  
  if computer_guess > number:
    high = computer_guess -1
  if computer_guess < number:
    low = computer_guess +1
    
  
  print(computer_guess)
  computer_guesses +=1
  

  

  if computer_guess == number:
    print("the computer has guessed the right number")
    print("it the the computer " + str(computer_guesses) + " guesses to guess the right number")
    active = False
    


