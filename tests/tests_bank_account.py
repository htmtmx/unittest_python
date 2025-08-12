import unittest

from src.bank_account import BankAccount


class BankAccountTests(unittest.TestCase):

    def test_deposit(self):
        account = BankAccount(initial_balance=1000)
        new_balance = account.deposit(500)
        self.assertEqual(new_balance, 1500)

    def test_withdraw(self):
        account = BankAccount(initial_balance=1000)
        new_balance = account.withdraw(300)
        self.assertEqual(new_balance, 700)

    def test_get_balance(self):
        account = BankAccount(initial_balance=1000)
        self.assertEqual(account.get_balance(), 1000)
