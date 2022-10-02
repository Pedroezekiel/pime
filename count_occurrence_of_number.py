import collections
user_input = input("Enter integers between 1 and 100")
lis = collections.Counter(user_input.split())
# counter = []
# # for i in lis:
# #     if i in counter:
# print(lis)
for i,y in lis.items():
    if y > 1:
        print(f"{i} occurs {y} times")
    else:
        print(f"{i} occurs {y} time")