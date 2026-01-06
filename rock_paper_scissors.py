import random


playerscore = 0
computerscore = 0


print('choose rock, paper, or scissors')


while True: 
  playerchoice = input('rock, paper, or  scissors?')
  computerchoice = random.choice(["rock","paper", "scissors"])
  
  
  print('you chose ' + playerchoice)
  print('the computer chose ' + computerchoice)
  
  if playerchoice == computerchoice:
    print('Tie!')
    
  if playerchoice == 'end':
    break
  
  if playerchoice == 'paper' and computerchoice == 'rock':
    print('You Win!')
    playerscore = playerscore + 1
  if playerchoice == 'rock' and computerchoice == 'paper':
    print('computer wins!')
    computerscore = computerscore + 1
  if playerchoice == 'scissors' and computerchoice == 'paper':
    print('you win!')
    playerscore = playerscore + 1
  if playerchoice == 'paper' and computerchoice == 'scissors':
    print('computer wins!')
    computerscore = computerscore + 1
  if playerchoice == 'rock' and computerchoice == 'scissors':
    print('you win!')
    playerscore = playerscore + 1
  if playerchoice == 'scissors' and computerchoice == 'rock':
    print('computer wins!')
    computerscore = computerscore + 1
    
  print('you have won ' + str(playerscore) + ' times')
  print('the computer has won ' + str(computerscore) + ' times\n')
  
  
