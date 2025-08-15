import os
import unittest

from src.bank_account import BankAccount


class BankAccountTests(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(initial_balance=1000, log_file='bank_account.txt')
        self.second_account = BankAccount(initial_balance=0)
        
    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

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
        self.account.transfer(self.second_account, 600)
        self.assertEqual(self.account.get_balance(), 400)
        self.assertEqual(self.second_account.get_balance(), 600)
        
    def test_transaction_log(self):
        self.account.deposit(3500)
        self.assertTrue(os.path.exists('bank_account.txt'))
