class Account:

    def __init__(self, name):
        self.balance = 0
        self.name = name

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("negative amount can not be deposited")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("negative amount can not be deposited")
        elif amount > self.balance:
            raise ValueError("you no get sense")
        else:
            self.balance -= amount

    def load_airtime(self, amount):
        self.balance -= amount
        pass

    def transfer(self, receiver_amount,receiver_accountNumber):
        self.balance -= receiver_amount
        receiver_accountNumber.deposit(receiver_amount)


