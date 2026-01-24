import unittest
from mbpp_577_code import last_Digit_Factorial

class TestLastDigitFactorial(unittest.TestCase):

    def test_last_Digit_Factorial_zero(self):
        self.assertEqual(last_Digit_Factorial(0), 1)

    def test_last_Digit_Factorial_one(self):
        self.assertEqual(last_Digit_Factorial(1), 1)

    def test_last_Digit_Factorial_two(self):
        self.assertEqual(last_Digit_Factorial(2), 2)

    def test_last_Digit_Factorial_three(self):
        self.assertEqual(last_Digit_Factorial(3), 6)

    def test_last_Digit_Factorial_four(self):
        self.assertEqual(last_Digit_Factorial(4), 4)

    def test_last_Digit_Factorial_five(self):
        self.assertEqual(last_Digit_Factorial(5), 0)

    def test_last_Digit_Factorial_six(self):
        self.assertEqual(last_Digit_Factorial(6), 0)

    def test_last_Digit_Factorial_seven(self):
        self.assertEqual(last_Digit_Factorial(7), 0)

    def test_last_Digit_Factorial_eight(self):
        self.assertEqual(last_Digit_Factorial(8), 0)

    def test_last_Digit_Factorial_nine(self):
        self.assertEqual(last_Digit_Factorial(9), 0)

    def test_last_Digit_Factorial_ten(self):
        self.assertEqual(last_Digit_Factorial(10), 0)
