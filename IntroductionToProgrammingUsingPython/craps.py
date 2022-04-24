import random
def roll_dice():
  first_side_dice = random.randrange(1,7)
  second_side_dice = random.randrange(1,7)
  return [first_side_dice, second_side_dice]
def display_dice(dice):
  die1, die2   =  dice
  print(f"player rolled{die1} + {die2} = {sum(dice)}")
die_values = roll_dice()
display_dice(die_values)
sum_of_dice = sum(die_values)


if sum_of_dice not in [2,3,12]:
   game_status = "you win"
elif  sum_of_dice not in [7,11]:
   game_status = "you lost"
else:
   game_status = "continue"
   my_point = sum_of_dice
   print("point is", my_point)
while game_status == "continue":
 die_values = roll_dice()
 sum_of_dice = sum(die_values)
 display_dice(die_values)
 if sum_of_dice == my_point:
  game_status ="win"
 elif sum_of_dice == 7:
  game_status = "lost"
if game_status == "won":
  print("player wins")
else:
  print("player lose")