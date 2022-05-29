# # num = [1,2,3,4]
# # for number in num:
# #     print(number)
#
# # lst =[ i == int(input("enter")) for i in range(10)  if i % 2 == 0]
# # print(lst)
#
# # lst = [chr(i) for i in range(65,91)]
# # print(lst)
#
# def sub(a,b):
#     return a - b
# def add (a,b):
#     return a+b
# def w (a,b,fn):
#     return fn(a,b)
# def mul(a,b):
#     return a*b
# def multiple(a,fn):
#     return fn(a)
# # print(w(1,23, lambda x,y: x-y))
# # print(w(1,23, lambda x,y: x/y))
# # print(w(1,23, lambda x,y: x+y))
# print(multiple(5,lambda x: 2 * x ) )
# print(multiple(10,lambda x: 2 * x ) )
#
#
# peoples =[{"name": "Omosetan Omorele", "age": 30, "year_of_exp": 4, "language":["python","java"] },
#           {"name": "John Doe", "age": 25, "year_of_exp": 2, "language":["JavaScript","c#"] },
#           {"name": "Amaka Stephen", "age": 19, "year_of_exp": 5, "language":["python"] },
#           {"name": "Florence segun", "age": 28, "year_of_exp": 15, "language":["python","java"] },
#            {"name": "Ernest Adeola", "age": 30, "year_of_exp": 4, "language":["kotlin","java"] }]
# print([ people["age"] <= 20 and "python".lower()   in people["language"] for  people in peoples])


# map_object = map(lambda x: x**2 if x%2 == 0 else x, range (1,10))
# list1 =list(map_object)
# list2 = list(map_object)
# print("1",list1)
# print("2",list2)

# from functools import reduce
#
# fruits = ["Apple", "pear", "pineapple", "orange", "watermelon", "banana", "cucumber"]
# longest = reduce(lambda x, y: x if len(x) > len(y) else y, fruits)
# longest = reduce(lambda x, y: x if len(x) > len(y) else y, fruits)
# print(longest)
# print(max(fruits, key=len))
# print(sorted(fruits, key=len, reverse=True))
# print(sorted(fruits, key=lambda x: x[-1]))
# print("Ne NEED""\n")
# print("TO LEARN PYTHON")
# print("AS QUICKLY AS POSSIBLE")


def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("At least you can see the function is 'divide'")
    else:
        return a // b


num = input("enter the numerator: ")
den = input("enter the denominator: ")

while True:
    try:
        num = int(num)
        den = int(den)
        print(divide(num, den))
        break


    except (ValueError, TypeError):
        print("Wrong input try again")
        num = int(input("enter the numerator: "))
        den = int(input("enter the denominator: "))
        continue
