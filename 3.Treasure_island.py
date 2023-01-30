print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction_raw=input('''\nWe are there! Which way, left or right? (type "left" for left and "right" for right): ''')
direction=direction_raw.lower()
if direction != "left":
  print("\nYou fell into a trap of the locals. Bad luck!\n\nGAME OVER")
else:
  crossing_the_river_raw=input('''\nGreat! You' ve reached the bank of a river.\nHow do you cross the river, by swimming or by waiting for the water to calm? (type ("swim" for swimming and "wait" for waiting): ''')
  crossing_the_river=crossing_the_river_raw.lower()
  if crossing_the_river != "wait":
    print ("You are too hasty! Crocodiles attack and eat you. Gruesome!\n\nGAME OVER")
  else:
    door_raw=input('''You' ve crossed the river successfully!\nNow there is an ancient building in front of you. You see three doors; one red, one blue, and one yellow. Which door do you open? (type "red" for the red door, "blue" for the blue door, and "yellow" for the yellow door): ''')
    door=door_raw.lower()
    if door != "yellow":
      print("Flesh-eating bugs attack and eat you. It seems everybody in this island are hungry for your flesh!n\nGAME OVER")
    else:
      print("\nYOU HAVE FOUND THE ANCIENT TREASURE. YOU ARE NOW RICH!\n\n\nBUT THE REAL TREASURE IS THE FRIENDS YOU' VE MADE ON THE WAY AND THE CREATURES THAT HAVEN'T EATEN YOU!\n\nCONGRATULATIONS! THANK FOR PLAYING!")