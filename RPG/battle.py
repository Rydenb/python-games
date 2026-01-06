import random
from enemy import *

gold = 0

class Battle:
  def __init__(self, player1, player2):
    self.player1 = player1
    self.player2 = player2
    self.damage = 2
    
  def __str__(self):
    line1 = "\nplayer " + self.name + "\nhealth = " + str(self.health) + "\nattack = " + str(self.attack)
    line2 = "\nability1 name:" + str(self.ability[0]) +" mana:" + str(self.ability[2]) + " damage:" + str(self.ability[1]) + "\n"
    line3 = "ability2 name:" + str(self.ability2[0]) +" mana:" + str(self.ability2[2]) + " damage:" + str(self.ability2[1])
    return line1 + line2 + line3
    return self.player1.name + " VS " + self.player2.name
  def start_battle(self): 
    global gold
    p2first = random.randint(0,10)%2 == 0
    print("\n" + self.player1.name + " has entered a battle with " + self.player2.name)
    
    while((self.player1.health > 0) and (self.player2.health > 0)):
      print(self.player1)
      print(self.player2)
      
      # while attack_choice != 1 or attack_choice != 2:
      #   try:
      #     attack_choice = input("\n type 1 to use punch, type 2 to use slice")
      enemy_scaler = round(random.uniform(1, 2), 2)
      print("the " + self.player2.name + " attacks")
      player2_damage = self.player2.attack*enemy_scaler
      self.player1.health -=  player2_damage
      if isinstance(self.player2, Bossconst):
        for i in self.player2.abilities:
          if random.random() > i[2]:
            self.player1.health -= i[1]
            break
      print("the " + self.player2.name + " does " + str(player2_damage) + " damage")
      attack_choice = input("\n type 1 to use punch, type 2 to use slice")
      if attack_choice == "1":
        if self.player1.mana >= self.player1.ability1[2]:
          damage = self.player1.ability1[1]
          self.player1.mana -= self.player1.ability1[2]
        else:
          print("not enough mana")
          continue
      if attack_choice == "2":
        if self.player1.mana >= self.player1.ability2[2]:
          damage = self.player1.ability2[1]*self.player1.weapon[1]
          self.player1.mana -= self.player1.ability2[2]
        else:
          print("not enough mana")
          continue
      try:
        self.player2.health -= int(damage)
        if random.randint(1,2) == 1:
          self.player1.mana += random.randint(5,15)
      except:
        print(damage)
        print(self.player2.health)
      
      if self.player1.health <= 0:
        print(self.player1.name + " loses")
        exit()
      if self.player2.health == 0:
        print(self.player2.name + " loses")
        print("mana:" + str(self.player1.mana)) 
        gold += random.randint(100,1000)
        print(self.player2.name + " dropped " + str(gold) + " gold")
