import random
from password_generator_oop import numbers, alphabet, symbols


class Main:
    symbol = symbols.Symbols(int(input("Enter number of symbols")))
    number = numbers.Number(int(input("Enter number of numbers")))
    alphabet = alphabet.Alphabet(int(input("Enter number of alphabet")))
    password = alphabet.user_number_input() + number.user_number_input() + symbol.user_number_input()
    random.shuffle(password)
    print("".join(map(str, password)))
