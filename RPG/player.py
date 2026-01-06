import sys

class playerconst:
  def __init__(self, name, weapon):
    color = "blue"
    self.health = 100
    self.attack = 1
    self.name = name
    self.mana = 100
    #3 ELEMENT OF LIST IS MANA 2ND IS DAMAGE
    self.ability1 = ["punch", 10, 5]
    self.ability2 = ["slice", 150, 125]
    self.weapon = weapon
    self.inventory = {
    self.weapon[0] : [weapon[1], weapon[2], 1]#weapon[0] is weapon name weapon[1] is the damage and weapon[2] is the durability, the thingn agter weapon[2] is the amount of potions you have 
  }
    self.gold = 100
    
    
  def __str__(self):
    spacer("-")
    line1 = "\nplayer " + self.name + "\nhealth = " + str(self.health) + "\nattack = " + str(self.attack) + "\nmana = " + str(self.mana)
    line2 = "\nability1 name:" + str(self.ability1[0]) +" mana:" + str(self.ability1[2]) + " damage:" + str(self.ability1[1]) + "\n"
    line3 = "ability2 name:" + str(self.ability2[0]) +" mana:" + str(self.ability2[2]) + " damage:" + str(self.ability2[1])
    spacer("-")
    line4 = str(self.inventory) + "(1st value = damage, second value = durability, third value = the amount of items you have)"
    return line1 + line2 + line3 + line4
    
    
def spacer(symbol):
  print
  for i in range(57):
    sys.stdout.write(symbol)
  print
