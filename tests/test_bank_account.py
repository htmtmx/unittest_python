import os
import unittest
from unittest.mock import patch

from src.bank_account import BankAccount
from src.exceptions import WithdrawalOutsideBusinessDaysError, WithdrawalOutsideBusinessHoursError

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

    @patch("src.bank_account.datetime")
    def test_withdraw(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.now.return_value.weekday = 4
        new_balance = self.account.withdraw(300)
        self.assertEqual(new_balance, 700)

    @patch("src.bank_account.datetime")
    def test_withdraw_after_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 20
        mock_datetime.now.return_value.weekday = 4
        with self.assertRaises(WithdrawalOutsideBusinessHoursError):
            self.account.withdraw(300)

    @patch("src.bank_account.datetime")
    def test_withdraw_before_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 5
        mock_datetime.now.return_value.weekday = 5
        with self.assertRaises(WithdrawalOutsideBusinessHoursError):
            self.account.withdraw(300)

    @patch("src.bank_account.datetime")
    def test_withdraw_in_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.now.return_value.weekday = 4
        self.assertTrue(self.account.withdraw(300))

    @patch("src.bank_account.datetime")
    def test_withdraw_in_business_days(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.now.return_value.weekday = 5
        new_balance = self.account.withdraw(300)
        self.assertEqual(new_balance, 700)

    @patch("src.bank_account.datetime")
    def test_withdraw_out_business_days(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.now.return_value.weekday = 6
        with self.assertRaises(WithdrawalOutsideBusinessDaysError):
            self.account.withdraw(300)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_transfer_with_no_founds(self):
        with self.assertRaises(ValueError):
            self.account.transfer(self.second_account, 1500)

    @patch("src.bank_account.datetime")
    def test_transfer_with_founds(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.now.return_value.weekday = 4
        self.account.transfer(self.second_account, 600)
        self.assertEqual(self.account.get_balance(), 400)
        self.assertEqual(self.second_account.get_balance(), 600)

    def test_transaction_log(self):
        self.account.deposit(3500)
        self.assertTrue(os.path.exists("bank_account.txt"))

    @patch("src.bank_account.datetime")
    def test_count_transactions(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.now.return_value.weekday = 4
        self.assertEqual(self._count_lines("bank_account.txt"), 1)
        self.account.deposit(3500)
        self.assertEqual(self._count_lines("bank_account.txt"), 2)
        self.account.withdraw(1000)
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

    def test_deposit_various_ammounts(self):
        test_cases = [
            {"ammount": 100, "expected": 1100},
            {"ammount": 3000, "expected": 4000},
            {"ammount": 4500, "expected": 5500},
        ]
        for case in test_cases:
            with self.subTest(case):
                self.account = BankAccount(initial_balance=1000, log_file="bank_account.txt")
                new_balance = self.account.deposit(case["ammount"])
                self.assertEqual(new_balance, case["expected"])
