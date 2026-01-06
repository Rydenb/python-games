from player import playerconst
from battle import Battle
from enemy import *
import sys
import time

def cprint(text, text_speed=0.0):
  for i in range(len(text)):
    time.sleep(text_speed)
    sys.stdout.write(text[i])
  print
# def loading(loading_time):
#   for i in range(loading_time):
#     time.sleep(0.01)
#     sys.stdout.write(".")
def menu():
  name = input("player name: ")
  cprint("\nwelcome to the world of Atheria " + name)
  cprint("\nyou have been recruited to investigate a village with a series of mysterious disappearances")
  cprint("\nyou find a wooden sword")
  weapon = ["wooden sword", 15, 43]#first entry:name second entry:damage thrid entry:durability
  player1 = playerconst(name, weapon)
  print player1
  path1(player1)
  
  keepAsking = True

def path1(player):
  cprint("\nyou see a bee hive", 0.02)
  beehive = enemyconst("beehive", 10, 2, 0)
  print beehive

  print(player)
  
  Queen_bee = Bossconst("Queen bee", 50, 10, 0)
  Queen_bee.teach_ability("Shoot Stinger", 30, 0.9)
  
  choice = input("\n1 for fight, 2 for flee")
  while choice == "1" or choice == "2":
    spacer("-")
    if choice == "1":
      battle1 = Battle(player, beehive)
      battle1.start_battle()
      break
      print(player)
    if choice =="2":
      player.health -= 10
      print("you lost 10 health while fleeing the battle, your health is now: " + str(player.health))
      break
    
  print(Queen_bee)
  while choice == "1" or choice == "2":
    spacer("-")
    if choice == "1":
      battle2 = Battle(player, Queen_bee)
      battle2.start_battle()
      break
      print(player)
    if choice =="2":
      player.health -= 50
      print("you lost 50 health while fleeing the battle, your health is now: " + str(player.health))
      break
    
  cprint("\nThe Queen Bee drops a scroll covered in honey, you decide to pick it up and look inside", 0.0000001)
  cprint("\nAs you open the honey-covered scroll, a magical inscription reveals a hidden path deep into the heart of the Enchanted Forest.")
  cprint("\nYou decide to follow the mystical trail, guided by the Queen Bee's honeyed magic.")
  print("you gained 100 health and 50 mana")
  player.health += 100
  player.mana += 60
  path2(player)  
def spacer(symbol):
  print
  for i in range(57):
    sys.stdout.write(symbol)
  print
    
def path2(player):
  global name
  print("As you enter the Enchanted Forest you hear ominous footsteps and you see a gigantic gorilla ")
  king_gorilla = Bossconst("King gorilla", 75, 15, 0)
  print(king_gorilla)
  battle3 = Battle(player, king_gorilla)
  battle3.start_battle()
 
  cprint("\nThe gorilla's death unleashes a vengeful spirit, forcing you to confront a new, even more formidable foe.")
  player.mana += 90
  player.health += 100
  mr_gorilla = Bossconst("mr_gorrilla", 130, 15, 0)
  mr_gorilla.teach_ability("heavy punch", 45, 0.80)
  print(mr_gorilla)
  battle4 = Battle(player, mr_gorilla)
  battle4.start_battle()
  
  
  print("Congratulations!, you have won\n\n")
  cprint("The Enchanted Forest falls silent as the last echoes of the vengeful spirit's defeat fade into the rustling leaves. You stand victorious, your heart pounding with the exertion of the battle. The forest itself seems to breathe a sigh of relief, its ancient trees swaying gently in the breeze. \n" "the hero of Atheria(you) returns to the village, bearing the honeyed scroll as a testament to their courage and resilience. The villagers celebrate your return with heartfelt gratitude and newfound hope. The mysterious disappearances have ceased, and life begins to blossom anew.", 0.01)

menu()
