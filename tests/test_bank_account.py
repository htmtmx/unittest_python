import os
import unittest

from src.bank_account import BankAccount
from src.exceptions import WithdrawalOutsideBusinessHoursError

SERVER = "server_a"


class BankAccountTests(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(initial_balance=1000, log_file="bank_account.txt")
        self.second_account = BankAccount(initial_balance=0)

    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename) as f:
            return len(f.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500)

    def test_withdraw(self):
        new_balance = self.account.withdraw(300, 10)
        self.assertEqual(new_balance, 700)

    def test_withdraw_outside_business_hours(self):
        with self.assertRaises(WithdrawalOutsideBusinessHoursError):
            self.account.withdraw(300, 20)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_transfer_with_no_founds(self):
        with self.assertRaises(ValueError):
            self.account.transfer(self.second_account, 1500, 10)

    def test_transfer_with_founds(self):
        self.account.transfer(self.second_account, 600, 10)
        self.assertEqual(self.account.get_balance(), 400)
        self.assertEqual(self.second_account.get_balance(), 600)

    def test_transaction_log(self):
        self.account.deposit(3500)
        self.assertTrue(os.path.exists("bank_account.txt"))

    def test_count_transactions(self):
        self.assertEqual(self._count_lines("bank_account.txt"), 1)
        self.account.deposit(3500)
        self.assertEqual(self._count_lines("bank_account.txt"), 2)
        self.account.withdraw(1000, 13)
        self.assertEqual(self._count_lines("bank_account.txt"), 3)

    @unittest.skip("Skipping this test for demonstration purposes")
    def test_skip_test(self):
        self.assertEqual(self.account.get_balance(), 400)

    @unittest.skipIf(SERVER == "server_a", "Skipping this test because we're on server_a")
    def test_skip_if(self):
        self.assertEqual(self.account.get_balance(), 400)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(self.account.get_balance(), 500)
