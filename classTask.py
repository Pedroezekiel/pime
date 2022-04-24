# user_input = input("Enter a number = ")
# first_number = int(user_input)
# if first_number % 2 == 0:
#      print(first_number, " is an even number")

# else:
#      print(first_number, " is an odd number")
# user_input = input("Enter a number = ")
# first_number = int(user_input)
# if first_number < 40:
#    print("f")
# elif first_number >= 40 and first_number <= 49:
#     print("D")
# elif first_number >= 50 and first_number <= 59:
#     print("C")
# elif first_number >= 60 and first_number <= 69:
#     print("B")
# elif first_number >= 70:
#     print("A")
# x = 1
# while x <= 5:
#     i = 1
#     while i <= 5:
#         print(i, end=" ")
#         i += 1
#     x += 1
#     print()
#

# x = 1
# while x <= 5:
#      i = x
#      while i <= 5:
#          print(" " , end=" ")
#          i += 1
#      i = 1
#      while i <= x:
#          print("#" , end=" ")
#          i += 1
#      x +=1
#      print()


# word = "hello"
# for letter in word:
#     print(letter)
#
# user_input = input("enter a number: ")
# number = int(user_input)
# factor = 1
# sum_of_factors = 0
# while factor <= (number // 2):
#     if number % factor == 0:
#      sum_of_factors += factor
#     factor += 1
# print(sum_of_factors)
#
# if sum_of_factors == number:
#     print(number, "is a perfect number")
# elif sum_of_factors > number:
#     print(number, "is an abundant number")
# else:
#     print(number, "is a deficient number")
#
# import math
# prime_number = int(input("enter a number"))
# math.ceil(math.sqrt(prime_number))
# #
# print("Welcome to the Band Name Generator")
# userInput1 = input("what's the name of the city you grew up in \n")
# userInput2 = input("What's your pet's name? \n")
# print(f"Your band name could be {userInput1} {userInput2}")
# #
#
# print("Welcome to the tip calculator")
# price = float(input("What was the total bill? $"))
# price_percentage = int(input("what percentage tip will you like to give? 10,12, or 15? "))
# spliting_of_bill = int(input("how many people should split the bill? "))
#
# tip = price_percentage / 100 * price
#
#
# total = (price + tip) / spliting_of_bill
# print(f"each person should pay: {round(total)} ")
# print("Welcome to the rollerCoaster")
# height = int(input("enter height \n"))
# bill = 0
# if(height > 120 ):
#      print("can ride rollerCoaster")
#      age = int(input("enter your age  \n"))
#      if(age < 12):
#          bill = 5
#          print("child tickets are $5")
#      elif(age >=12 and age <=18 ):
#          bill = 7
#          print("youth tickets are $7")
#      elif(age < 45):
#           bill = 12
#           print("adult tickets are $12")
#      elif(age > 45 and age <= 55):
#          bill = 0
#          print("elderly are free")
#      want_pictures=(input("do you want pictures Y or N  \n"))
#      if(want_pictures=="yes"):
#          bill += 3
#          print(f"your total bill is ${bill}")

# else:
#     print("sorry you have to grow taller to ride rollerCoaster")
# print("Welcome to even or odd")
# number = int(input("Enter a number for checking if is even or odd\n"))
# if(number%2 == 0):
#     print("Number is even")
# else:
#     print("Number is odd")
# firstNumber = int(input("enter first number \n"))
# secondNumber = int(input("enter second number \n"))
# answer = firstNumber/secondNumber
# print(f"{firstNumber} / {secondNumber} = {round(answer)}")
# if round(answer) %  2 == 0 :
#     print("answer is even ")
# else:
#     print("answer is odd")

# print("leap year")
# year = int(input("enter a year to check if it is a leap year or not \n"))
# if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
#     print(f"The year {year} is a leap year")
# else:
#     print(f"The year {year} is not a leap year")
# print("Welcome to python pizza deliveries")
# size = input("What size pizza do you want ? S, M, or L \n")
# add_pepperoni = input("Do you want pepperoni? Y or N  \n")
# extra_cheese = input("Do you want extra cheese? Y or N \n")
# price = 0
# if size == "S":
#     price = 15
#     print(f"small pizza = ${price}")
#     if add_pepperoni == "Y":
#         print("pepperoni for Small pizza: +$2")
#         price += 2
#         print(f"small pizza and pepperoni = ${price}")
#     if extra_cheese == "Y":
#         price += 1
#         print("extra chess is + $1")
#     print(f"Your final bill is: ${price}")
# elif size == "M":
#     price = 20
#     print(f"Medium pizza = ${price}")
#     if add_pepperoni == "Y":
#        print("pepperoni for Medium pizza: +$3")
#        price += 3
#        print(f"Medium pizza and pepperoni = {price}")
#     if extra_cheese == "Y":
#             price += 1
#             print("extra chess is + $1")
#             print(f"Your final bill is: ${price}")
# elif size == "L":
#     price = 25
#     print(f"Large pizza = ${price}")
#     if add_pepperoni == "Y":
#         print("pepperoni for Large price is + $3")
#         price += 3
#         print(f"Large pizza and pepperoni = ${price}")
#     if extra_cheese == "Y":
#      price += 1
#      print("extra chess is + $1")
#     print(f"Your final bill is: ${price}")

# print("welcome to love calculator")
# name1 = input("what is your name? \n")
# name2 = input("what is their name \n")
#
# t = name1.count("t") + name2.count("t")
# r = name1.count("r") + name2.count("r")
# u = name1.count("u") + name2.count("u")
# e = name1.count("e") + name2.count("e")
# true = t+r+u+e
#
# l = name1.count("l") + name2.count("l")
# o = name1.count("o") + name2.count("o")
# v = name1.count("v") + name2.count("v")
# e = name1.count("e") + name2.count("e")
# love = l+o+v+e
#
# your_true_love = int(str(true)+str(love))
#
# if your_true_love < 10 or your_true_love > 90:
#     print(f"your score is {your_true_love}, you go together like coke and mentos")
# elif your_true_love > 40 < 50:
#     print(f"your score is {your_true_love}, you are alright together")
# else:
#     print(f"your score is {your_true_love}")

# star = "*"
# for i in range"(1,11):
#    print(f"{star * i:<10} {star * (11 - i):<10} {star * (11 - i):>10} {star * i:>10}")
# print("""
# ***********************
# welcome to my store
# ************************""")
# products = ["maggi", " salt", "rice"]
# prices =   [10, 50, 300]
# quantities = []
# colums =["products", "quantities", "prices", "totals"]
# print(f"{colums[0]:>15} |  {colums[1]:>2} | {colums[2]:>6}")
# i = 0
# while i < len(products):
#     quantities.append(int(input(products[i])))
#     i += 1
# i = 0
# while i < len(products):
#     print(f"{products[i]:>15}  |  {quantities[i]:>2} ")
#
# for product in products:
#     a = product
#     print(a[0]       , end=" ")
#     print()
# for quantity in  quantities:
#      b = quantity
#      print(b)
# for price in prices:
#     c = price
#     print(c)

# for total in totals:
#     c = total
#     add_up += int(total)
#     print(c)
# print(add_up)

# def do_something(lst: list) -> None:
#     lst[1] = 100
#
# a = [ 1, 2, 3, 4, ]
# do_something(a)
# print(a)
# n = 0
# number = int(input("enter a num"))
# print("number","\t", "square", "\t\t", "cube")
# while number >= n:
#     print(f"{n:>10}{n*n:>13}{n*n*n:>19}")
#
#     n += 1
# grade = int(input())
# result = "passed" if grade >= 60 else "falied"
# print(result)
# total = 0
# grade_counter = 0
#
# grade = int(input("Enter grade, -1 to end: "))
#
# while grade != -1:
#      total +=grade
#      grade_counter += 1
#      grade = int(input("enter grade, -1 to end: "))
# if grade_counter != 0:
#      average = total / grade_counter
#      print(f"Class average is {average: .2f}")
# else:
#      print("No grades were entered")

# def add(a: int = 2, b: str = "color") -> tuple[int, str]:
#     return a, b
#
#
# print(add(3, "3"))
# print(add(3))
# print(add())
# print(add(b=5, a="you"))
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# print([[x,y,z] for x in range (n) if n != [3] for y in range (n) if n!= [3] for z in range (n) ])
# x = 2
# y = 2
# z = 2
# n = 2
#
#
# lst = []
# for x in range (n):
#     for y in range(n):
#         for z in range(n):
#                 lst.append([x,y,z])
# print(lst)
import random
word_list =["ardvark", "baboon", "camel"]
legnth =len(word_list)
chosen_word = random.randint(0 ,legnth-1)
c = word_list[chosen_word]
print(f"psst, the solution is {c}.")
display = [ ]
k = random.choice(word_list)
c = display.append(k)
for letter in k:
    print("_",end=" ")
print()
guess = str(input("guess a letter")).lower()
for cs in c:
    result = cs if guess == cs else cs
    print(result )
#
