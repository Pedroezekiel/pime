# print("Convert pounds into pounds")
# pounds = float(input("Enter a value in pounds\n"))
# kilogram = 0.454
# print(f"{pounds} pounds is {pounds*kilogram} kilogram")

# print("Convert celsius to Fahrenheit")
# celsius = int(input("Enter a degree in Celsius: "))
# fahrenheit = (9 / 5) * celsius + 32
# print(f"{celsius} celsius is {fahrenheit} fahrenheit")

# print("Compute the volume of a cylinder")
# radius , length = float(input("enter the radius and length of a cylinder")),int(input("the length"))
# area = (radius * radius) * 3.14
# volume = area * length
# print(f"The area is {round(area)}")
# print(f"The volume is {round(volume)}")

# print("Convert feet into meters")
# feet = float(input("Enter a value for feet: "))
# meters = 0.305
# print(f"{feet} feet is {feet*meters} meters")

# print("Financial application: calculate tip")
# subtotal = float(input("Enter the subtotal: "))
# gratuity_rate = int(input("Enter a gratuity rate: "))
# gratuity = subtotal * gratuity_rate / 100
# total =  gratuity + subtotal
# print(f"The gratuity is {gratuity} and the total is {total}")

# print("Convert pounds into kilograms")
# pounds = float(input("Enter a value in pounds: "))
# kilograms = 0.454
# print(f"{pounds} pounds is {pounds*kilograms} kilograms")
#
# numbers = (input("Enter a number"))
# total = 0
# for number in numbers:
#     total += int(number)
# print(total,)

# import random
#
# names = input("enter names of buyers: \n").split(", ")
# length = len(names)
# random_choice = random.randint(0,length-1)
# person_who_will_names = names[random_choice]
# print(person_who_will_names,"will pay for the meal today")

# student_scores = (input("enter student score:' \n")).split(" ")
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# max = 0
# min = 0
#
# for student_score  in   student_scores:
#     # max = int(student_score)
#     # for max in student_scores:
#       if student_score > max:
#        max = student_score
# print("The highest score in the class is:", max)
# for student_score in student_scores:
#       if student_score < min:
#           min  = student_score
# print("The lowest score in the class is:",min)
#

# def get_digit(number: int, position: int) -> int:
#     """
#     Get the digit at a particular position
#
#     >>> get_digit(234, 0)
#     4
#     >>> get_digit(234, 2)
#     2
#     >>> "hello"
#     'hello'
#     >>> "2" + 3 # doctest: +IGNORE_EXCEPTION_DETAIL
#     Traceback(most recent call last):
#
#     """
#     return number // (10 ** position) % 10
#
#
# v = get_digit(1029,0)
# print(v)
numbers = [1, 2, 3, 4, 5]
num = numbers.count([0],len(numbers))
for num in numbers:
    print(num,end=" ")