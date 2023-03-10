import random

class Player:
  def __init__(self):
    self.inventory = ["BARE HANDS"]
    self.currentposition = [4,0]

  def print_inventory(self):
    print("Inventory: ", self.inventory)

  def print_location(self):
    print("Current position: ", self.currentposition)

  def move(self, newcoord):
    self.currentposition = newcoord

  def take(self, item):
    self.inventory.append(item)
    
  def drop(self, item):
    if item in self.inventory:
      self.inventory.remove(item)
      print(item.lower(), "dropped.")
    else:
      print("You don't have the "+ item.lower() +"!")

  def can_visit(self, newcoord):
    if (newcoord[0]==3 and newcoord[1]==1):
      return False and print("There is a wall blocking your path.")
    elif (newcoord[0]==4 and newcoord[1]==2):
      return False and print("There is a wall blocking your path.")
    else:
      return True
  
  def process_item(self, item):
    if item == 'SWORD' or item == 'ROCK' or item == 'ARMOR' or item == 'KEY' or item == 'MONSTER':
      print("You see a " + item.lower() + ".")
    elif item == 'EXIT':
      pass

  def determine_item(self):
    return input("What would you like to drop? ").upper()

  def map_edge(self):
    print("You cannot move here.") 


class Map:
  def __init__(self):
    self.map = [["ARMOR"," "," ", "EXIT"],[" ","SWORD"," "," "],[" "," ","TREE"," "],["ROCK","WALL"," ","MONSTERr"],["START"," ","WALL","KEY"]]
    self.useful = ["BARE HANDS","ARMOR","KEY","SWORD","ROCK"]
  
player = Player()
map = Map()
###################
#    Game Loop    #
###################

gameRunning = True
while gameRunning:
  direction = input("What would you like to do?  ").upper()
  if direction == "UP":
    if not player.currentposition[0]==0:
      newcoord = [player.currentposition[0]-1,player.currentposition[1]]
      if player.can_visit(newcoord):
        player.move(newcoord)
        player.process_item(map.map[newcoord[0]][newcoord[1]])
    else:
      player.map_edge()

  #elif direction == "DOWN":
  #  if not player.currentposition[0]==4:
  #    newcoord = [player.currentposition[0]+1,(player.currentposition[1])]
  #    if(player.can_visit(newcoord)):
  #      player.currentposition = newcoord
  #  else:
  #    print("You cannot move here.")
  #elif direction == "LEFT":
  #  if not player.currentposition[1]==0:
  #    newcoord = [player.currentposition[1],(player.currentposition[0]-1)]
  #    if(player.can_visit(newcoord)):
  #      player.currentposition = newcoord
  #  else:
  #    print("You cannot move here.")
  #elif direction == "RIGHT":
  #  if not player.currentposition[1]==3:
  #    newcoord = [player.currentposition[1],(player.currentposition[0]+1)]
  #    if(player.can_visit(newcoord)):
  #      player.currentposition = newcoord

  elif direction == "TAKE":
    if len(player.inventory) < 3:
      player.take(map.map[newcoord[0]][newcoord[1]])
    else:
      print("Your inventory is full. Drop an item to take this " + map.map[newcoord[0]][newcoord[1]])
  elif direction == "DROP":
    player.drop(player.determine_item())
  elif direction == "INVENTORY":
    player.print_inventory()
  elif direction == "LOCATION":
    player.print_location()
  else:
      print("This is not a valid instruction.")
  
#in game loop, include picking up/dropping items. refer to map function to tell which items are "useable". also write code for defeating the monster. 