from random import randint

number = randint(1,100)
guesses = 10


print("The Number Guessing Game")
while True:
  difficulty = input('choose a difficulty, easy, medium, hard, or extremely hard')
  if difficulty == "easy":
    guesses = 10
    break
  if difficulty == "medium":
    guesses = 5
    break
  if difficulty == "hard":
    guesses = 3
    break
  if difficulty == "extremely hard":
    guesses = 1
    break
for i in range(guesses):
  guess = input('guess a number 1-100')
  guess = int(guess)
  if guess == number:
    print('You win! You have guessed the right number')
    break
  else:
    guesses = guesses - 1
    
  if guess > number:
    print('your guess was to high')
    if guesses >1:
      print('you have ' +str(guesses) + ' guesses left')
    
    if guesses == 1:
       print('you have ' +str(guesses) + ' guess left')
  if guess < number:
    print('your guess was to low')
    
    if guesses >1:
      print('you have ' +str(guesses) + ' guesses left')
    
    if guesses == 1:
       print('you have ' +str(guesses) + ' guess left')
    
    
if guesses == 0:
  print('you have lost the number was ' +str(number))
    
    

