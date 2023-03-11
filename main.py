import random

class Player:
  def __init__(self):
    self.inventory=["BARE HANDS"]
    self.currentPosition=[4,0]
    self.defeatedMonster=False
    self.commands=["UP", "DOWN", "LEFT", "RIGHT", "TAKE", "USE", "DROP", "INVENTORY", "LOCATION", "HELP"]

  def print_commands(self):
    print("Valid commands are: ")
    print(self.commands)

  def print_inventory(self):
    print("Inventory: "+str(self.inventory))

  def get_location(self):
    return self.currentPosition

  def print_location(self):
    print("Current position: "+str(self.currentPosition))

  def move(self, newcoord):
    self.currentPosition=newcoord

  def take(self, item):
    self.inventory.append(item)
    # if item!="TREE" and item!="MONSTER":
    #   if item not in self.inventory:
    #     self.inventory.append(item)
    #   elif item in self.inventory:
    #     print("You already have the "+item.lower()+ " in your inventory.")
    # else:
    #   print("You cannot take the "+item.lower()+" into your inventory.")
    
  def drop(self, item):
    if item in self.inventory:
      self.inventory.remove(item)
      print(item.lower()+" dropped.")
    else:
      print("You don't have the "+item.lower()+"!")

  def visit(self, newcoord, map):
    if (newcoord[0]==3 and newcoord[1]==1) or (newcoord[0]==4 and newcoord[1]==2):
      print("There is a wall blocking your path.")
    elif (newcoord[0]==4 and newcoord[1]==3):
      if self.defeatedMonster:
        self.move(newcoord)
        return self.process_item(map.map[newcoord[0]][newcoord[1]])
      else:
        print("You must defeat the monster before moving to this part of the map.")
    else:
      self.move(newcoord)
      return self.process_item(map.map[newcoord[0]][newcoord[1]])
    return True

  def process_item(self, item):
    if item==" " or item=="START":
        print("You see nothing.")
    elif item=="EXIT":
      if "KEY" in self.inventory:
        print("Congratulations! You have successfully completed your mission!")
        return False
      else:
        print("You need a key to exit.")
    else:
      print("You see the "+item.lower()+".")
    return True

  def determine_item(self):
    return input("What would you like to drop? ").upper()

  def weapon_result(self, weapon, map):
    if weapon=="SWORD":
      if "ARMOR" in self.inventory:
        print("You used the sword and defeated the monster!")
        map.map[player.currentPosition[0]][player.currentPosition[1]]=" "
        return True
      else:
        probability=random.randint(1,4)
        if probability==4:
          print("You were defeated by the monster.")
          return False
        else:
          print("You used the sword and defeated the monster!")
          map.map[player.currentPosition[0]][player.currentPosition[1]]=" "
          return True
    elif weapon=="ROCK":
      if "ARMOR" in self.inventory:
        probability=random.randint(1,4)
        if probability==1 or probability==2:
          print("You used the rock and defeated the monster!")
          map.map[player.currentPosition[0]][player.currentPosition[1]]=" "
          return True
        else:
          print("You were defeated by the monster.")
          return False
      else:
        probability=random.randint(1,4)
        if probability==1:
          print("You used the rock and defeated the monster!")
          map.map[player.currentPosition[0]][player.currentPosition[1]]=" "
          return True
        else:
          print("You were defeated by the monster.")
          return False
    elif weapon=="BARE HANDS":
      if "ARMOR" in self.inventory:
        probability=random.randint(1,4)
        if probability==1:
          print("You used your bare hands and defeated the monster!")
          map.map[player.currentPosition[0]][player.currentPosition[1]]=" "
          return True
      else:
        print("You were defeated by the monster.")
        return False

  def use_weapon(self):
    if len(self.inventory)>0:
      weapon=input("What would you like to use? ").upper()
      if weapon in self.inventory:
        #return self.weapon_result(weapon, map)
        self.defeatedMonster=self.weapon_result(weapon, map)
      else:
        print("You do not have a "+weapon.lower()+".")
    else:
      print("You have no weapons to use.")

  def map_edge(self):
    print("You cannot move here.")

class Map:
  def __init__(self):
    self.map=[["ARMOR"," "," ", "EXIT"],[" ","SWORD"," "," "],[" "," ","TREE"," "],["ROCK","WALL"," ","MONSTER"],["START"," ","WALL","KEY"]]
    self.useful=["BARE HANDS", "ARMOR", "KEY", "SWORD", "ROCK"]
  
player=Player()
map=Map()

###################
#    Game Loop    #
###################
gameRunning=True
while gameRunning:
  direction=input("What would you like to do?  ").upper()
  coord=player.get_location()
  item=map.map[coord[0]][coord[1]]
  if direction=="UP":
    if not coord[0]==0:
      gameRunning=player.visit([coord[0]-1,coord[1]], map)
    else:
      player.map_edge()
  elif direction=="DOWN":
    if not coord[0]==4:
      gameRunning=player.visit([coord[0]+1,coord[1]], map)
    else:
      player.map_edge()
  elif direction=="LEFT":
    if not coord[1]==0:
      gameRunning=player.visit([coord[0],coord[1]-1], map)
    else:
      player.map_edge()
  elif direction=="RIGHT":
    if not coord[1]==3:
      gameRunning=player.visit([coord[0], coord[1]+1], map)
    else:
      player.map_edge()
  elif direction=="TAKE":
    if item in map.useful:
      if len(player.inventory)<3: 
        player.take(item)
        map.map[player.currentPosition[0]][player.currentPosition[1]]=" "
        print("The "+item.lower()+" is now in your inventory.")
      else:
        print("Your inventory is full. Drop an item to take this "+item.lower()+".")
      # if item!=" ":
      #   print("The "+item.lower()+" is not useable as a weapon.")
    else:
      print("There is nothing to take.")
  elif direction=="DROP":
    player.drop(input("What would you like to drop?  ").upper())
  elif direction=="USE":
    if coord[0]==3 and coord[1]==3:
      player.use_weapon()
    else:
      print("You cannot use a weapon on a "+item.lower()+".")
  elif direction=="INVENTORY":
    player.print_inventory()
  elif direction=="LOCATION":
    player.print_location()
  elif direction=="HELP":
    player.print_commands()
  else:
    print("That is not a valid command.") 
