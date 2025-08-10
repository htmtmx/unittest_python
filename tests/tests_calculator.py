import unittest

from src.calculator import addition, division, multiplication, substraction


class CalculatorTest(unittest.TestCase):
    # setUp is called before every test
    def setUp(self):
        self.a = 10
        self.b = 5

    def test_sum(self):
        self.assertEqual(addition(self.a, self.b), 15, "Are not equal")

    def test_substract(self):
        self.assertEqual(substraction(self.a, self.b), 5, "Are not equal")

    def test_multiplication(self):
        self.assertEqual(multiplication(self.a, self.b), 50, "Are not equal")

    def test_division_by_zero(self):
        exception_raised = False
        try:
            division(3, 0)
        except ZeroDivisionError:
            exception_raised = True
        self.assertTrue(exception_raised)

    def test_division(self):
        self.assertEqual(division(self.a, self.b), 2, "Are not equal")


if __name__ == "__main__":
    unittest.main()
