# def custom_for(iterable,fun):
#     it = iter(iterable)
#
#     while True:
#         try:
#             fun(next(it))
#         except StopIteration:
#                 break
#
#
# custom_for([1, 35, 7, 9],print)
# def gen():
#     counter = 0
#     if counter ==5:
#
#     while True:
#         yield counter
#         counter += 1
# def counter(low,high,step):
#     while low <= high:
#         yield low
#         low += step
#
# print(list(counter(1,10,4)))

# for i in gen():
#     print(i)

# from collections import Counter
#
# x = "i am a boy i am a a"
# x_counter = Counter(x.split())
#
# for i,y  in x_counter.items():
#     print(f"{i  } | {  y}")
import  collections
Person = collections.namedtuple("person", "name age")
p1 = Person(name="Adam", age=30)
print(p1.name)