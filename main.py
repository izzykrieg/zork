import random

class Player:
  def __init__(self):
    self.inventory = ["Bare hands"]
    self.currentposition = (4,0)

  def print_inventory(self):
    self.print("Inventory: ", self.inventory)

  def print_location(self):
    print("Current position: ", self.currentposition)

  def move_adj(self, newcoord):
    self.currentposition = newcoord
    pass

  def take(self, item):
    self.inventory.append(item)
    
  def drop(self, item):
    if item in self.inventory:
      self.inventory.remove(item)
      print(item, " dropped.")
    else:
      print("You don't have the "+ item +"!")

  def can_visit(newcoord):
    if (newcoord[0]==3 and newcoord[1]==1):
      return False and print("That is a wall.")
    elif (newcoord[0]==4 and newcoord[1]==2):
      return False and print("That is a wall.")
    else:
      return True
      #pass

class Map:
  def __init__(self):
    self.map = [["Armor"," "," ", "Exit"],[" ","Sword"," "," "],[" "," ","Tree"," "],["Rock","Wall"," ","Monster"],["Start"," ","Wall","Key"]]
    self.useful = ["Bare hands","Armor","Key","Sword","Rock"]
  
player = Player()
map = Map()
###################
#    Game Loop    #
###################

gameRunning = True
while gameRunning:
  direction = input("What direction would you like to go?  ")


  if direction == "up" or "Up" or "UP":
    if not player.currentposition[0]==0:
      newcoord =             (player.currentposition[0]-1,player.currentposition[1])
      if(player.can_visit(newcoord)):
        player.currentposition = newcoord

  if direction == "down" or "Down" or "DOWN":
    if not player.currentposition[0]==4:
      newcoord = [player.currentposition[0]+1,(player.currentposition[1])]
      if(player.can_visit(newcoord)):
        player.currentposition = newcoord
  if direction == "left" or "Left" or "LEFT":
    if not player.currentposition[1]==0:
      newcoord = [player.currentposition[1],(player.currentposition[0]-1)]
      if(player.can_visit(newcoord)):
        player.currentposition = newcoord
  if direction == "right" or "Right" or "RIGHT":
    if not player.currentposition[1]==3:
      newcoord = [player.currentposition[1],(player.currentposition[0]+1)]
      if(player.can_visit(newcoord)):
        player.currentposition = newcoord
#in game loop, include picking up/dropping items. refer to map function to tell which items are "useable". also write code for defeating the monster. 