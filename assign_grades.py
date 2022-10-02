a = input( " Enter")
x = a.split()
print(int(max(x)))
for i in range(len(x)):
    if int(x[i]) >= int(max(x))- 10:
        print(f"Student {i} is {x[i]} and grade is A")
    elif int(x[i]) >=  int(max(x)) - 20:
        print(f"Student {i} is {x[i]} and grade is B")
    elif int(x[i]) >= int(max(x))- 30:
        print(f"Student {i} is {x[i]} and grade is C")
    elif int(x[i]) >= int(max(x))-40:
        print(f"Student {i} is {x[i]} and grade is D")
    else:
        print(f"Student {i} is {x[i]} and grade is F")