import random


def roll_dice():
    dice1 = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)
    return dice1, dice2


def display_dice(rolled_dice):
    dice1, dice2 = rolled_dice
    print(f"{dice1} + {dice2} = {sum(rolled_dice)}")


rolled_dice_value = roll_dice()
display_dice(rolled_dice_value)
sum_of_the_rolled_dice = sum(rolled_dice_value)

if sum_of_the_rolled_dice in [11, 7]:
    game_status = "WIN"
elif sum_of_the_rolled_dice in [2, 3, 12]:
    game_status = "LOST"
else:
    game_status = "CONTINUE"
    point = sum_of_the_rolled_dice

while game_status == "CONTINUE":
    rolled_dice_value = roll_dice()
    display_dice(rolled_dice_value)
    sum_of_the_rolled_dice = sum(rolled_dice_value)
    if sum_of_the_rolled_dice == 7:
        game_status = "LOST"
    elif sum_of_the_rolled_dice == point:
        game_status = "WIN"
if game_status == "LOST":
    print("you loses\ntry again")
elif game_status == "WIN":
    print("my oga\nyou win")
