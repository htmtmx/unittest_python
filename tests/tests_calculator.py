import unittest

from src.calculator import addition, division, multiplication, substraction


class CalculatorTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(addition(2, 3), 5, "Are not equal")

    def test_substract(self):
        self.assertEqual(substraction(5, 3), 2, "Are not equal")

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 5), 15, "Are not equal")

    def test_division_by_zero(self):
        exception_raised = False
        try:
            division(3, 0)
        except ZeroDivisionError:
            exception_raised = True
        self.assertTrue(exception_raised)

    def test_division(self):
        self.assertEqual(division(20, 5), 4, "Are not equal")


if __name__ == "__main__":
    unittest.main()
