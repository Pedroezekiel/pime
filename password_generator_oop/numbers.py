import random


class Number:
    number_password = []

    def __init__(self, number_of_numbers):
        self.number_of_numbers = number_of_numbers

    def user_number_input(self):
        for i in range(self.number_of_numbers):
            self.number_password.append(random.randint(0, 9))
        return self.number_password


