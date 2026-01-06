from random import *

good_letters = []
bad_letters = []

#reads the text file "words.txt" and stores it as list lines
with open('words.txt', 'r')as f:
  lines = f.readlines()
#uses a loop to run through the list and get rid of the \n that is on every word
for i in range(len(lines)):
  lines[i] = lines[i].strip('\n')
  lines[i] = lines[i].lower()#makes things all lowercase

#create a word processing function to process a word
def WordProcessing(word):
  #creates an empty string
  newWord = ' '
  #uses a for loop to run through the program
  for i in word:
    newWord = newWord + '_ '
  return newWord
  
#gets random word from word list
word = lines[randint(0, len(lines)-1)]
print (WordProcessing(word))
print('choose a word')
attempts = 0
#create a dictionary of all letters in the word
letter_list = {}
for i in enumerate(word):
  char = i[1]
  letter_list[char] = 0
#print(letter_list)
for i in enumerate(word):
  char = i[1]
  letter_list[char] += 1
  #print(letter_list)
  
#print(word)
  
win = False

while attempts <= 6:
  guess = input()
  if guess == word:
    win = True
    break
  if guess == 'Tell me the word':
    print('The word is ' + word)
  if guess in lines:
    attempts += 1
    pass
  else:
    print('invalid guess')
    continue
  currword = ''
  for i in enumerate(guess):
    char = guess[i[0]]
    if char == word[i[0]]:
      print((str(char)) +  ' is in the spot of the word')
      currword += char
      letter_list[char] -= 1
      #print(letter_list)

    elif char in word:
      if letter_list[char] > 0:
        print((str(char)) + ' is in the word')
        good_letters.append(char)
        currword += '_ '
      else:
        print((str(char)) + ' is not in the word')
        bad_letters.append(char)
        currword += '_ '
    else:
      print((char) + ' is not in the word')
      bad_letters.append(char)
      currword += '_ '
  print('good letters:' + str(good_letters) +'\nbad letters:' + str(bad_letters))
  print(currword)
  
print('the word was ' + word)
if win == True:
  print('You win!')
else:
  print('you lose')
    
    
  
