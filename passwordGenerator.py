import random

passwords = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
             ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ".", "/", "-", ".", "`"],
             ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x",
              "c", "v", "b", "n", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J",
              "K", "L", "Z", "X", "C", "V", "B", "N", "M"]]
user_input_letter = int(input("How many letter would you like in your password? "))
user_input_symbols = int(input("How many symbols would you like? "))
user_input_numbers = int(input("How many numbers would you like? "))
length2 = len(passwords[2][1:])
length3 = len(passwords[1][1:])
random_choice2 = random.randint(0, length2 - 1)
random_choice3 = random.randint(0, 8)
random_choice4 = random.randint(0, length3 - 1)
# random_choice = (random.randint(0,length2 - 1),random.randint(0,length3-1),random.randint(   0,8))
letter = passwords[2][1:][random_choice2]
number = passwords[0][1:][random_choice3]
symbols = passwords[1][1:][random_choice4]
# add_up = passwords[0:][random_choice]
length0 = 0
password_list = []
for password in passwords[2][1:]:
    if user_input_letter > length0:
        password_list.append(letter)
        user_input_letter -= 1
        random_choice2 = random.randint(0, length2 - 1)
        letter = passwords[2][1:][random_choice2]
for password in passwords[0][1:]:
    if user_input_numbers > length0:
        password_list.append(str(number))
        user_input_numbers -= 1
        random_choice4 = random.randint(0, 8)
        number = passwords[0][1:][random_choice3]
for password in passwords[1][1:]:
    if user_input_symbols > length0:
        password_list.append(symbols)
        user_input_symbols -= 1
        random_choice4 = random.randint(0, length3 - 1)
        symbols = passwords[1][1:][random_choice4]

random.shuffle(password_list)
print(''.join(password_list))
