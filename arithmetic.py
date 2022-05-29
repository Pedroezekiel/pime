import random

userinput = input("what level do you want to play 1.Easy, 2Hard : ")
userinput2 = input("what type of arithmetic problem do you want \n1. addition 2.subtraction 3.multiplication "
                   "4.division 5. mixture: ")

x = random.randint(1, 2)
y = random.randint(1, 2)

if x < y:
    x, y = y, x


def correct():
    correct = ["Very good!", "Nice work", "Keep up the good good"]
    correct_random_choice = random.choice(correct)
    return correct_random_choice


def multiplication() -> None:
    if int(input(f'{x} X {y} = ')) == x * y:
        print(correct())
    else:
        print(wrong())
        for i in range(1000000):
            if int(input(f'{x} X {y} = ')) == x * y:
                print(correct())
                break
            else:
                print(wrong())
            continue


def division():
    if int(input(f'{x} / {y} = ')) == x / y:
        print(correct())
    else:
        print(wrong())
        for i in range(1000000):
            if int(input(f'{x} / {y} = ')) == x / y:
                print(correct())
                break
            else:
                print(wrong())
            continue


def addition():
    if int(input(f'{x} + {y} = ')) == x + y:
        print(correct())
    else:
        print(wrong())
        for i in range(1000000):
            if int(input(f'{x} + {y} = ')) == x + y:
                print(correct())
                break
            else:
                print(wrong())
            continue


def subtraction():
    if int(input(f'{x} - {y} = ')) == x - y:
        print(correct())
    else:
        print(wrong())
        for i in range(1000000):
            if int(input(f'{x} - {y} = ')) == x - y:
                print(correct())
                break
            else:
                print(wrong())
            continue


def mixture():
    if userinput2 == '5':
        arithmetic = ["x + y", "x / y", "x - y", "x X y"]
        random_symbols = random.choice(arithmetic)
        if random_symbols == "x + y":
            addition()
        elif random_symbols == "x - y":
            subtraction()
        elif random_symbols == "x / y":
            division()
        else:
            multiplication()


def wrong():
    wrong = ["No. please try again", "Wrong try once more", "No. keep trying"]
    wrong_random_choice = random.choice(wrong)
    return wrong_random_choice


if userinput == "1":
    for i in range(1000):
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        if x < y:
            x, y = y, x
        if userinput2 == "3":
            multiplication()
        elif userinput2 == "1":
            addition()
        elif userinput2 == "4":
            division()
        elif userinput2 == "2":
            subtraction()
        elif userinput2 == '5':
            mixture()

elif userinput == "2":
    for i in range(1000):
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        if x < y:
            x, y = y, x
        if userinput2 == "3":
            addition()
            subtraction()
            multiplication()
            division()
            mixture()

else:
    for i in range(1000000):
        correct = ["Very good!", "Nice work", "Keep up the good good"]
        correct_random_choice = random.choice(correct)
        wrong = ["wrong", "Try once more", "No. keep trying"]
        wrong_random_choice = random.choice(wrong)
        print(wrong_random_choice)
        u = int(input(f"{x} x {y} = "))
        if u == x * y:
            print(correct_random_choice)
            break
        else:
            continue
