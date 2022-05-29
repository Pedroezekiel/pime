import random


def animals_tortoise():
    tortoise = random.randint(1, 10)
    if 1 <= tortoise <= 5:
        movement = "Fast plod"
        actual_move = "3 squares to the right"
    elif 6 <= tortoise <= 7:
        movement = "Slip"
        actual_move = "6 squares to the left"
    elif 8 <= tortoise <= 10:
        movement = "slow plod"
        actual_move = "1 square to the right"
    return movement


def animal_hare():
    hare = random.randint(1, 10)
    if 1 <= hare <= 2:
        movement = "sleep"
        actual_move = "No move"
    elif 3 <= hare <= 4:
        movement = "Big hop"
        actual_move = "9 squares to the right"
    elif hare == 5:
        movement = "Big slip"
        actual_move = "12 squares to the left"
    elif 6 <= hare <= 8:
        movement = "Small hop"
        actual_move = "1 square to the right"
    elif 9 <= hare <= 10:
        movement = "Small slip"
        actual_move = "2 square to the left"
    return movement


print("""Bang ! ! ! !
 AND THEY'RE OFF  ! ! ! ! !""")
move = " "
for x in range(1, 71):
    t = animals_tortoise()
    h = animal_hare()
    if t == "Fast plod":
        T = "   T"
    elif t == "Slip":
        T = "T      "
    elif t == "slow plod":
        T = " T"
    else:
        T = ""
    if h == "No move":
        H = end = ""
    elif h == "Big hop":
        H = "         H"
    elif h == "Big slip":
        H = "H            "
    elif h == "Small hop":
        H = " H"
    else:
        H = "H  "
    if T == " T" and H == " H":
        T = "ou"
        H = "ch"

    else:
        h = ""
        print(f"{T}{H}")
if T >= str(70):
    print("tortoise win")
elif H >= str(70):
    print("hare win")
else:
    print("tie")