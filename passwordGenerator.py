import random
passwords_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                  ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ".", "/", "-", ".", "`"],
                  ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z",
                   "x",
                   "c", "v", "b", "n", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H",
                   "J",
                   "K", "L", "Z", "X", "C", "V", "B", "N", "M"]]
numbers_of_number = int(input("Enter number of number: "))
numbers_of_symbol = int(input("Enter number of symbol: "))
numbers_of_alphabeth = int(input("Enter number of alphabeth: "))
passwords = []
for i in range(numbers_of_number):
    generated_password =random.choice(passwords_list[0])
    passwords.append(generated_password)
for i in range(numbers_of_symbol):
    generated_password = random.choice(passwords_list[1])
    passwords.append(generated_password)
for i in range(numbers_of_alphabeth):
    generated_password = random.choice(passwords_list[2])
    passwords.append(generated_password)
random.shuffle(passwords)
for i in passwords:
    print(i,end="")