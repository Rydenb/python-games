class enemyconst:
  def __init__(self, name, health, attack, defense):
    self.name = name
    self.health = health
    self.attack = attack
    self.defense = defense
    self.isBoss = False
  def __str__(self):
    return "enemy " + self.name + "\nhealth = " + str(self.health) + "\nattack = " + str(self.attack) + "\ndefense = " + str(self.defense)
    
class Bossconst(enemyconst):
  def __init__(self, name, health, attack, defense):
    super().__init__(name, health, attack, defense)
    self.abilities = []
    self.isBoss = True
  def teach_ability(self, name, damage, chance):
    self.abilities.append([name, damage, chance])
      
