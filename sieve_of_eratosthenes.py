import math
number = 20
counter = 0
while counter < number:
    counter += 1
    x = math.ceil(counter/2)
    # print(x,end=" ")
    # print(f'{counter}//{x} = {counter%x}')
    if counter == 2:
        print(counter)

    if counter % x != 0:
        print(counter)

