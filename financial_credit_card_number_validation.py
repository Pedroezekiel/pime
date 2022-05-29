def adding(x):
    sum = 0
    for digit in str(x):
        sum += int(digit)
    return sum


card_number = [4, 3, 8, 8, 5, 7, 6, 0, 1, 8, 4, 1, 0, 7, 0, 7]
c = []
n = []
for number in reversed(card_number[::2]):
    result = number * 2
    if result > 9:
        c.append(adding(result))
    else:
        c.append(result)
print(sum(c))
for number in card_number[1::2]:
    n.append(number)
print(sum(n))
result = sum(c) + sum(n)
if result % 10 == 0:
    print("Valid")
else:
    print("Invalid")