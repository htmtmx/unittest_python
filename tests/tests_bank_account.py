import unittest

from src.bank_account import BankAccount


class BankAccountTests(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(initial_balance=1000)
        self.second_account = BankAccount(initial_balance=0)

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500)

    def test_withdraw(self):
        new_balance = self.account.withdraw(300)
        self.assertEqual(new_balance, 700)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_transfer_with_no_founds(self):
        with self.assertRaises(ValueError):
            self.account.transfer(self.second_account, 1500)

    def test_transfer_with_founds(self):
        self.account.transfer(self.second_account, 500)
        self.assertEqual(self.account.get_balance(), 500)
        self.assertEqual(self.second_account.get_balance(), 500)
