import string
import random


class Alphabet:
    alphabet_password = []
    lower_alphabet = list(string.ascii_lowercase)
    upper_alphabet = list(string.ascii_uppercase)
    alphabet =lower_alphabet+upper_alphabet

    def __init__(self, number_of_alphabet):
        self.number_of_alphabet = number_of_alphabet

    def user_number_input(self):
        for i in range(self.number_of_alphabet):
            self.alphabet_password.append(random.choice(self.alphabet))
        return self.alphabet_password


