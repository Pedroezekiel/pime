import unittest
from . import account


class AccountTest(unittest.TestCase):
    def test_that_account_has_a_name(self):
        account1 = account.Account("Ezekiel")
        self.assertEqual("Ezekiel", account1.name)

    def test_that_account_has_a_balance(self):
        account1 = account.Account("Ezekiel")
        self.assertEqual(0, account1.balance)

    def test_that_account_can_deposit(self):
        account1 = account.Account("Ezekiel")
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)

    def test_that_account_cannot_deposit_negative_amount(self):
        account1 = account.Account("Ezekiel")
        account1.deposit(200)
        self.assertRaises(ValueError, account1.deposit, -2500)

    def test_that_account_can_withdraw(self):
        account1 = account.Account("Ezekiel")
        account1.deposit(2000)
        account1.withdraw(2000)
        self.assertEqual(0, account1.balance)

    def test_that_account_can_not_withdraw_more_than_the_money_in_the_account(self):
        account1 = account.Account("Ezekiel")
        account1.deposit(2000)
        self.assertRaises(ValueError, account1.withdraw, 2100)

    def test_that_account_can_load_airtime(self):
        account1 = account.Account("Ezekiel")
        account1.deposit(200)
        account1.load_airtime(100)
        self.assertEqual(100,account1.balance)

    def test_that_account_can_transfer(self):
        account1 = account.Account("Ezekiel")
        account2 = account.Account("Enny")
        account1.deposit(200)
        self.assertEqual(200, account1.balance)
        account1.transfer(200, account2)
        self.assertEqual(200, account2.balance)
