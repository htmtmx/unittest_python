import unittest

from tests.test_bank_account import BankAccountTests

def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTests('test_deposit'))
    suite.addTest(BankAccountTests('test_withdraw'))
    suite.addTest(BankAccountTests('test_get_balance'))
    suite.addTest(BankAccountTests('test_transfer_with_no_founds'))
    suite.addTest(BankAccountTests('test_transfer_with_founds'))
    suite.addTest(BankAccountTests('test_transaction_log'))
    suite.addTest(BankAccountTests('test_count_transactions'))
    suite.addTest(BankAccountTests('test_skip_test'))
    suite.addTest(BankAccountTests('test_skip_if'))
    suite.addTest(BankAccountTests('test_expected_failure'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())
