# # user_input = input("Enter a number = ")
# # first_number = int(user_input)
# # if first_number % 2 == 0:
# #      print(first_number, " is an even number")
#
# # else:
# #      print(first_number, " is an odd number")
# # user_input = input("Enter a number = ")
# # first_number = int(user_input)
# # if first_number < 40:
# #    print("f")
# # elif first_number >= 40 and first_number <= 49:
# #     print("D")
# # elif first_number >= 50 and first_number <= 59:
# #     print("C")
# # elif first_number >= 60 and first_number <= 69:
# #     print("B")
# # elif first_number >= 70:
# #     print("A")
# # x = 1
# # while x <= 5:
# #     i = 1
# #     while i <= 5:
# #         print(i, end=" ")
# #         i += 1
# #     x += 1
# #     print()
# #
#
# # x = 1
# # while x <= 5:
# #      i = x
# #      while i <= 5:
# #          print(" " , end=" ")
# #          i += 1
# #      i = 1
# #      while i <= x:
# #          print("#" , end=" ")
# #          i += 1
# #      x +=1
# #      print()
#
#
# # word = "hello"
# # for letter in word:
# #     print(letter)
# #
# # user_input = input("enter a number: ")
# # number = int(user_input)
# # factor = 1
# # sum_of_factors = 0
# # while factor <= (number // 2):
# #     if number % factor == 0:
# #      sum_of_factors += factor
# #     factor += 1
# # print(sum_of_factors)
# #
# # if sum_of_factors == number:
# #     print(number, "is a perfect number")
# # elif sum_of_factors > number:
# #     print(number, "is an abundant number")
# # else:
# #     print(number, "is a deficient number")
# #
# # import math
# # prime_number = int(input("enter a number"))
# # math.ceil(math.sqrt(prime_number))
# # #
# # print("Welcome to the Band Name Generator")
# # userInput1 = input("what's the name of the city you grew up in \n")
# # userInput2 = input("What's your pet's name? \n")
# # print(f"Your band name could be {userInput1} {userInput2}")
# # #
# #
# # print("Welcome to the tip calculator")
# # price = float(input("What was the total bill? $"))
# # price_percentage = int(input("what percentage tip will you like to give? 10,12, or 15? "))
# # spliting_of_bill = int(input("how many people should split the bill? "))
# #
# # tip = price_percentage / 100 * price
# #
# #
# # total = (price + tip) / spliting_of_bill
# # print(f"each person should pay: {round(total)} ")
# # print("Welcome to the rollerCoaster")
# # height = int(input("enter height \n"))
# # bill = 0
# # if(height > 120 ):
# #      print("can ride rollerCoaster")
# #      age = int(input("enter your age  \n"))
# #      if(age < 12):
# #          bill = 5
# #          print("child tickets are $5")
# #      elif(age >=12 and age <=18 ):
# #          bill = 7
# #          print("youth tickets are $7")
# #      elif(age < 45):
# #           bill = 12
# #           print("adult tickets are $12")
# #      elif(age > 45 and age <= 55):
# #          bill = 0
# #          print("elderly are free")
# #      want_pictures=(input("do you want pictures Y or N  \n"))
# #      if(want_pictures=="yes"):
# #          bill += 3
# #          print(f"your total bill is ${bill}")
#
# # else:
# #     print("sorry you have to grow taller to ride rollerCoaster")
# # print("Welcome to even or odd")
# # number = int(input("Enter a number for checking if is even or odd\n"))
# # if(number%2 == 0):
# #     print("Number is even")
# # else:
# #     print("Number is odd")
# # firstNumber = int(input("enter first number \n"))
# # secondNumber = int(input("enter second number \n"))
# # answer = firstNumber/secondNumber
# # print(f"{firstNumber} / {secondNumber} = {round(answer)}")
# # if round(answer) %  2 == 0 :
# #     print("answer is even ")
# # else:
# #     print("answer is odd")
#
# # print("leap year")
# # year = int(input("enter a year to check if it is a leap year or not \n"))
# # if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
# #     print(f"The year {year} is a leap year")
# # else:
# #     print(f"The year {year} is not a leap year")
# # print("Welcome to python pizza deliveries")
# # size = input("What size pizza do you want ? S, M, or L \n")
# # add_pepperoni = input("Do you want pepperoni? Y or N  \n")
# # extra_cheese = input("Do you want extra cheese? Y or N \n")
# # price = 0
# # if size == "S":
# #     price = 15
# #     print(f"small pizza = ${price}")
# #     if add_pepperoni == "Y":
# #         print("pepperoni for Small pizza: +$2")
# #         price += 2
# #         print(f"small pizza and pepperoni = ${price}")
# #     if extra_cheese == "Y":
# #         price += 1
# #         print("extra chess is + $1")
# #     print(f"Your final bill is: ${price}")
# # elif size == "M":
# #     price = 20
# #     print(f"Medium pizza = ${price}")
# #     if add_pepperoni == "Y":
# #        print("pepperoni for Medium pizza: +$3")
# #        price += 3
# #        print(f"Medium pizza and pepperoni = {price}")
# #     if extra_cheese == "Y":
# #             price += 1
# #             print("extra chess is + $1")
# #             print(f"Your final bill is: ${price}")
# # elif size == "L":
# #     price = 25
# #     print(f"Large pizza = ${price}")
# #     if add_pepperoni == "Y":
# #         print("pepperoni for Large price is + $3")
# #         price += 3
# #         print(f"Large pizza and pepperoni = ${price}")
# #     if extra_cheese == "Y":
# #      price += 1
# #      print("extra chess is + $1")
# #     print(f"Your final bill is: ${price}")
#
# # print("welcome to love calculator")
# # name1 = input("what is your name? \n")
# # name2 = input("what is their name \n")
# #
# # t = name1.count("t") + name2.count("t")
# # r = name1.count("r") + name2.count("r")
# # u = name1.count("u") + name2.count("u")
# # e = name1.count("e") + name2.count("e")
# # true = t+r+u+e
# #
# # l = name1.count("l") + name2.count("l")
# # o = name1.count("o") + name2.count("o")
# # v = name1.count("v") + name2.count("v")
# # e = name1.count("e") + name2.count("e")
# # love = l+o+v+e
# #
# # your_true_love = int(str(true)+str(love))
# #
# # if your_true_love < 10 or your_true_love > 90:
# #     print(f"your score is {your_true_love}, you go together like coke and mentos")
# # elif your_true_love > 40 < 50:
# #     print(f"your score is {your_true_love}, you are alright together")
# # else:
# #     print(f"your score is {your_true_love}")
#
# # star = "*"
# # for i in range"(1,11):
# #    print(f"{star * i:<10} {star * (11 - i):<10} {star * (11 - i):>10} {star * i:>10}")
# # print("""
# # ***********************
# # welcome to my store
# # ************************""")
# # products = ["maggi", " salt", "rice"]
# # prices =   [10, 50, 300]
# # quantities = []
# # colums =["products", "quantities", "prices", "totals"]
# # print(f"{colums[0]:>15} |  {colums[1]:>2} | {colums[2]:>6}")
# # i = 0
# # while i < len(products):
# #     quantities.append(int(input(products[i])))
# #     i += 1
# # i = 0
# # while i < len(products):
# #     print(f"{products[i]:>15}  |  {quantities[i]:>2} ")
# #
# # for product in products:
# #     a = product
# #     print(a[0]       , end=" ")
# #     print()
# # for quantity in  quantities:
# #      b = quantity
# #      print(b)
# # for price in prices:
# #     c = price
# #     print(c)
#
# # for total in totals:
# #     c = total
# #     add_up += int(total)
# #     print(c)
# # print(add_up)
#
# # def do_something(lst: list) -> None:
# #     lst[1] = 100
# #
# # a = [ 1, 2, 3, 4, ]
# # do_something(a)
# # print(a)
# # n = 0
# # number = int(input("enter a num"))
# # print("number","\t", "square", "\t\t", "cube")
# # while number >= n:
# #     print(f"{n:>10}{n*n:>13}{n*n*n:>19}")
# #
# #     n += 1
# # grade = int(input())
# # result = "passed" if grade >= 60 else "falied"
# # print(result)
# # total = 0
# # grade_counter = 0
# #
# # grade = int(input("Enter grade, -1 to end: "))
# #
# # while grade != -1:
# #      total +=grade
# #      grade_counter += 1
# #      grade = int(input("enter grade, -1 to end: "))
# # if grade_counter != 0:
# #      average = total / grade_counter
# #      print(f"Class average is {average: .2f}")
# # else:
# #      print("No grades were entered")
#
# # def add(a: int = 2, b: str = "color") -> tuple[int, str]:
# #     return a, b
# #
# #
# # print(add(3, "3"))
# # print(add(3))
# # print(add())
# # print(add(b=5, a="you"))
# # x = int(input())
# # y = int(input())
# # z = int(input())
# # n = int(input())
# # print([[x,y,z] for x in range (n) if n != [3] for y in range (n) if n!= [3] for z in range (n) ])
# # x = 2
# # y = 2
# # z = 2
# # n = 2
# #
# #
# # lst = []
# # for x in range (n)
# #     for y in range(n):
# #         for z in range(n):
# #                 lst.append([x,y,z])
# # print(lst)
# # import random
# #
# #
# # def animals_tortoise():
# #     tortoise = random.randint(1, 10)
# #     if 1 <= tortoise <= 5:
# #         movement = "Fast plod"
# #         actual_move = "3 squares to the right"
# #     elif 6 <= tortoise <= 7:
# #         movement = "Slip"
# #         actual_move = "6 squares to the left"
# #     elif 8 <= tortoise <= 10:
# #         movement = "slow plod"
# #         actual_move = "1 square to the right"
# #     return movement
# #
# #
# # def animal_hare():
# #     hare = random.randint(1, 10)
# #     if 1 <= hare <= 2:
# #         movement = "sleep"
# #         actual_move = "No move"
# #     elif 3 <= hare <= 4:
# #         movement = "Big hop"
# #         actual_move = "9 squares to the right"
# #     elif hare == 5:
# #         movement = "Big slip"
# #         actual_move = "12 squares to the left"
# #     elif 6 <= hare <= 8:
# #         movement = "Small hop"
# #         actual_move = "1 square to the right"
# #     elif 9 <= hare <= 10:
# #         movement = "Small slip"
# #         actual_move = "2 square to the left"
# #     return movement
# #
# #
# # print("""Bang ! ! ! !
# #  AND THEY'RE OFF  ! ! ! ! !""")
# # move = " "
# # for x in range(1, 71):
# #     t = animals_tortoise()
# #     h = animal_hare()
# #     if t == "Fast plod":
# #         T = "   T"
# #     elif t == "Slip":
# #         T = "T      "
# #     elif t == "slow plod":
# #         T = " T"
# #     else:
# #         T = ""
# #     if h == "No move":
# #         H = end = ""
# #     elif h == "Big hop":
# #         H = "         H"
# #     elif h == "Big slip":
# #         H = "H            "
# #     elif h == "Small hop":
# #         H = " H"
# #     else:
# #         H = "H  "
# #     if T == " T" and H == " H":
# #         T = "ou"
# #         H = "ch"
# #
# #     else:
# #         h = ""
# #         print(f"{T}{H}")
# # if T >= str(70):
# #     print("tortoise win")
# # elif H >= str(70):
# #     print("hare win")
# # else:
# #     print("tie")
#
# # import random
# #
# # userinput = input("what level do you want to play 1.Easy, 2Hard : ")
# # userinput2 = input("what type of arithmetic problem do you want \n1. addition 2.subtraction 3.multiplication "
# #                    "4.division 5. mixture: ")
# #
# # x = random.randint(1, 2)
# # y = random.randint(1, 2)
# #
# #
# # def correct():
# #     correct = ["Very good!", "Nice work", "Keep up the good good"]
# #     correct_random_choice = random.choice(correct)
# #     return correct_random_choice
# #
# #
# # def multiplication() -> None:
# #     if userinput2 == "3":
# #         if int(input(f'{x} X {y} = ')) == x * y:
# #             print(correct())
# #         else:
# #             print(wrong())
# #             for i in range(1000000):
# #                 if int(input(f'{x} X {y} = ')) == x * y:
# #                     print(correct())
# #                     break
# #                 else:
# #                     print(wrong())
# #                 continue
# #
# #
# # def division():
# #     if userinput2 == "4":
# #         if int(input(f'{x} / {y} = ')) == x / y:
# #             print(correct())
# #         else:
# #             print(wrong())
# #             for i in range(1000000):
# #                 if int(input(f'{x} / {y} = ')) == x / y:
# #                     print(correct())
# #                     break
# #                 else:
# #                     print(wrong())
# #                 continue
# #
# #
# # def addition():
# #     if userinput2 == "1":
# #         if int(input(f'{x} + {y} = ')) == x + y:
# #             print(correct())
# #         else:
# #             print(wrong())
# #             for i in range(1000000):
# #                 if int(input(f'{x} + {y} = ')) == x + y:
# #                     print(correct())
# #                     break
# #                 else:
# #                     print(wrong())
# #                 continue
# #
# #
# # def subtraction():
# #     if userinput2 == "2":
# #         if int(input(f'{x} - {y} = ')) == x - y:
# #             print(correct())
# #         else:
# #             print(wrong())
# #             for i in range(1000000):
# #                 if int(input(f'{x} - {y} = ')) == x - y:
# #                     print(correct())
# #                     break
# #                 else:
# #                     print(wrong())
# #                 continue
# #
# #
# # def mixture():
# #     if userinput2 == '5':
# #         arithmetic = ["x + y", "x / y", "x - y", "x X y"]
# #         random_symbols = random.choice(arithmetic)
# #         if random_symbols == "x + y":
# #             if int(input(f'{x} + {y} = ')) == x + y:
# #                 print(correct())
# #             else:
# #                 print(wrong())
# #                 for i in range(1000000):
# #                     if int(input(f'{x} + {y} = ')) == x + y:
# #                         print(correct())
# #                         break
# #                     else:
# #                         print(wrong())
# #                     continue
# #         elif random_symbols == "x - y":
# #             if int(input(f'{x} - {y} = ')) == x - y:
# #                 print(correct())
# #             else:
# #                 print(wrong())
# #                 for i in range(1000000):
# #                     if int(input(f'{x} - {y} = ')) == x - y:
# #                         print(correct())
# #                         break
# #                     else:
# #                         print(wrong())
# #                     continue
# #
# #         elif random_symbols == "x / y":
# #             if userinput2 == "4":
# #                 if int(input(f'{x} / {y} = ')) == x / y:
# #                     print(correct())
# #                 else:
# #                     print(wrong())
# #                     for i in range(1000000):
# #                         if int(input(f'{x} / {y} = ')) == x / y:
# #                             print(correct())
# #                             break
# #                         else:
# #                             print(wrong())
# #                         continue
# #         else:
# #             if userinput2 == "3":
# #                 if int(input(f'{x} X {y} = ')) == x * y:
# #                     print(correct())
# #                 else:
# #                     print(wrong())
# #                     for i in range(1000000):
# #                         if int(input(f'{x} X {y} = ')) == x * y:
# #                             print(correct())
# #                             break
# #                         else:
# #                             print(wrong())
# #                         continue
# #
# #
# # def wrong():
# #     wrong = ["No. please try again", "Wrong try once more", "No. keep trying"]
# #     wrong_random_choice = random.choice(wrong)
# #     return wrong_random_choice
# #
# #
# # if userinput == "1":
# #     for i in range(1000):
# #         x = random.randint(1, 9)
# #         y = random.randint(1, 9)
# #         multiplication()
# #         addition()
# #         division()
# #         subtraction()
# #         mixture()
# #
# # elif userinput == "2":
# #     for i in range(1000):
# #         x = random.randint(10, 99)
# #         y = random.randint(10, 99)
# #         if userinput2 == "3":
# #             addition()
# #             subtraction()
# #             multiplication()
# #             division()
# #             mixture()
# #
# # else:
# #     for i in range(1000000):
# #         correct = ["Very good!", "Nice work", "Keep up the good good"]
# #         correct_random_choice = random.choice(correct)
# #         wrong = ["wrong", "Try once more", "No. keep trying"]
# #         wrong_random_choice = random.choice(wrong)
# #         print(wrong_random_choice)
# #         u = int(input(f"{x} x {y} = "))
# #         if u == x * y:
# #             print(correct_random_choice)
# #             break
# #         else:
# #             continue
# # num = [2,3,3,4,5,5,6,6,7,7,8,9]
# # cot = []
# # for i in num:
# #     if i not in cot:
# #         cot.append(i)
# #  print(cot)
#
# # def apply_discount(product, discount):
# #     price = int(product['price'] * (1.0 - discount))
# #     assert 0 <= price <= product['price']
# #     return price
# #
# #
# # shoes = {'name': 'Fancy Shoes', 'price': 14900}
# #
# # print(apply_discount(shoes, 0.5))
#
# # def cube_list(value):
# #     for i in range(len(value)):
# #         value[i] **=3
# #     return value
# #
# #
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(cube_list(numbers))
#
# # numbers = [10, 3, 7, 1, 9, 4, 2,]
# # for value in [x ** 2 for x in numbers if x % 2 != 0]:
# #  print(value, end=' ')
# #
# # number = [10, 3, 7, 1, 9, 4, 2]
# # for value in (x for x in number if x % 2 == 0):
# #      print(value**3, end=" ")
# # for i in number:
# #     if i % 2 == 0:
# #         print(i, end=" ")
# #     else:
# #         pass
#
# # def num(number):
# #     number_list = {"1": "boy", "2" : "girl"}
# #     if len(number) == 1:
# #         return list(number_list[number[0]])
# #     else:
# #         result = num(number[:-1])
# #     return [(ch1 + ch2) for ch1 in result for ch2 in number_list[number[-1]]]
# #
# #
# # print(num("12"))
# # list_of_number = []
# #
# #
# # def numbers(userinput):
# #     if userinput == 1:
# #         return list_of_number.append(userinput[0])
# #     else:
# #         result = numbers(userinput[:-1])
# #     return [(ch1 + ch2) for ch1 in list_of_number for ch2 in result]
# #
# #
# #
# # print(numbers("123"))
#
#
lis = [["empty", "empty", "<empty>"], ["<empty>", "<empty>", "<empty>"], ["<empty>", "<empty>", "<empty>"]]
counter = 0

while True:
    while counter < 5:
        userinput = input("enter something")
        if userinput == "1":
            lis[0].remove(lis[0][0])
            lis[0].insert(0, "x")
            print(lis)
        elif userinput == "2":
            lis[0].remove(lis[0][1])
            lis[0].insert(1, "x")
            print(lis)
        elif userinput == "3":
            lis[0].remove(lis[0][2])
            lis[0].insert(2, "x")
            print(lis)
        elif userinput == "4":
            lis[1].remove(lis[1][0])
            lis[1].insert(0, "x")
            print(lis)
        elif userinput == "5":
            lis[1].remove(lis[1][2])
            lis[1].insert(1, "x")
            print(lis)
        elif userinput == "6":
            lis[1].remove(lis[1][2])
            lis[1].insert(2, "x")
            print(lis)
        elif userinput == "7":
            lis[2].remove(lis[2][0])
            lis[2].insert(0, "x")
            print(lis)
        elif userinput == "8":
            lis[2].remove(lis[2][1])
            lis[2].insert(1, "x")
            print(lis)
        elif userinput == "9":
            lis[2].remove(lis[2][2])
            lis[2].insert(2, "x")
            print(lis)
        userinput2 = input("enter something")
        if userinput2 == "1":
            lis[0].remove(lis[0][0])
            lis[0].insert(0, "o")
            print(lis)
        elif userinput2 == "2":
            lis[0].remove(lis[0][1])
            lis[0].insert(1, "o")
            print(lis)
        elif userinput2 == "3":
            lis[0].remove(lis[0][2])
            lis[0].insert(2, "o")
            print(lis)
        elif userinput2 == "4":
            lis[1].remove(lis[1][0])
            lis[1].insert(0, "o")
            print(lis)
        elif userinput2 == "5":
            lis[1].remove(lis[1][2])
            lis[1].insert(1, "o")
            print(lis)
        elif userinput2 == "6":
            lis[1].remove(lis[1][2])
            lis[1].insert(2, "o")
            print(lis)
        elif userinput2 == "7":
            lis[2].remove(lis[2][0])
            lis[2].insert(0, "o")
            print(lis)
        elif userinput2 == "8":
            lis[2].remove(lis[2][1])
            lis[2].insert(1, "o")
            print(lis)
        elif userinput2 == "9":
            lis[2].remove(lis[2][2])
            lis[2].insert(2, "o")
            print(lis)
        else:
            print()
