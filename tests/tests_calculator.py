import unittest

from src.calculator import addition, division, multiplication, substraction


class CalculatorTest(unittest.TestCase):
    def test_sum(self):
        assert addition(2, 3) == 5

    def test_substract(self):
        assert substraction(5, 3) == 2

    def test_multiplication(self):
        assert multiplication(3, 5) == 15

    def test_division_by_zero(self):
        exception_raised = False
        try:
            division(3, 0)
        except ZeroDivisionError:
            exception_raised = True
        assert exception_raised

    def test_division(self):
        assert division(20, 5) == 4
