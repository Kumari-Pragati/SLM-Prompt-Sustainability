import unittest
from mbpp_577_code import last_Digit_Factorial

class TestLastDigitFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(last_Digit_Factorial(0), 1)

    def test_positive_single_digit(self):
        self.assertEqual(last_Digit_Factorial(1), 1)
        self.assertEqual(last_Digit_Factorial(2), 2)
        self.assertEqual(last_Digit_Factorial(3), 6)
        self.assertEqual(last_Digit_Factorial(4), 4)

    def test_large_number(self):
        self.assertEqual(last_Digit_Factorial(5), 0)

    def test_negative_number(self):
        self.assertEqual(last_Digit_Factorial(-1), 0)

    def test_non_integer(self):
        self.assertEqual(last_Digit_Factorial(2.5), 0)
