import unittest
from mbpp_577_code import last_Digit_Factorial

class TestLastDigitFactorial(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(last_Digit_Factorial(0), 1)

    def test_one(self):
        self.assertEqual(last_Digit_Factorial(1), 1)

    def test_two(self):
        self.assertEqual(last_Digit_Factorial(2), 2)

    def test_three(self):
        self.assertEqual(last_Digit_Factorial(3), 6)

    def test_four(self):
        self.assertEqual(last_Digit_Factorial(4), 4)

    def test_five(self):
        self.assertEqual(last_Digit_Factorial(5), 5)

    def test_negative_number(self):
        self.assertEqual(last_Digit_Factorial(-1), 0)

    def test_large_number(self):
        self.assertEqual(last_Digit_Factorial(100), 0)
