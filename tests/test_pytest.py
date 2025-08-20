import pytest

from src.bank_account import BankAccount


@pytest.mark.parametrize(
    "ammount, expected",
    [
        (100, 1100),
        (3000, 4000),
        (4500, 5500),
    ],
)
def test_deposit_various_ammounts(ammount, expected):
    account = BankAccount(initial_balance=1000, log_file="bank_account.txt")
    new_balance = account.deposit(ammount)
    assert new_balance == expected


def test_sum():
    a = 4
    b = 5
    assert a + b == 9
