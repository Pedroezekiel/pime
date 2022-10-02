import random


class Symbols:
    symbol_password = []

    def __init__(self, number_of_symbols):
        self.number_of_symbols = number_of_symbols
        self.all_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ".", "/", "-", ".", "`", "[", "]", "+",
                            "="]

    def user_number_input(self):
        for i in range(self.number_of_symbols):
            self.symbol_password.append(random.choice(self.all_symbols))
        return self.symbol_password



