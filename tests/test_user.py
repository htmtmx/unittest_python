import os
import unittest

from faker import Faker

from src.bank_account import BankAccount
from src.user import User


class UserTests(unittest.TestCase):

    def setUp(self):
        self.faker = Faker(locale="es")
        self.user = User(name=self.faker.name(), email=self.faker.email())

    def tearDown(self):
        for account in self.user.accounts:
            os.remove(account.log_file)

    def test_user_creation(self):
        name_generated = self.faker.name()
        email_generated = self.faker.email()
        user = User(name=name_generated, email=email_generated)
        print(user.name)
        self.assertIsNotNone(user.name)
        self.assertEqual(user.name, name_generated)
        self.assertIsNotNone(user.email)
        self.assertEqual(user.email, email_generated)

    def test_user_with_multiple_accounts(self):
        # Data that must be created without using the Faker library
        # ammount_list = [
        #     {'ammount': 1000},
        #     {'ammount': 2000},
        #     {'ammount': 3000},
        # ]

        for _ in range(3):
            # Without Faker
            # bank_account = BankAccount(
            # initial_balance=ammount_list[_]['ammount'],
            # log_file='bank_account.txt')

            # With Faker
            bank_account = BankAccount(
                initial_balance=self.faker.random_int(min=1000, max=5000, step=100),
                log_file=self.faker.file_name(extension="txt"),
            )
            self.user.add_account(bank_account)

        expected_value = self.user.get_total_balance()
        value = sum(account.balance for account in self.user.accounts)
        self.assertEqual(value, expected_value)
