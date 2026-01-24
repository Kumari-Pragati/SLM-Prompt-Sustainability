import unittest
from mbpp_577_code import last_Digit_Factorial

class TestLastDigitFactorial(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(last_Digit_Factorial(0), 1)

    def test_one_to_three(self):
        self.assertEqual(last_Digit_Factorial(1), 1)
        self.assertEqual(last_Digit_Factorial(2), 2)
        self.assertEqual(last_Digit_Factorial(3), 6)

    def test_four(self):
        self.assertEqual(last_Digit_Factorial(4), 4)

    def test_five_and_above(self):
        self.assertEqual(last_Digit_Factorial(5), 0)
        self.assertEqual(last_Digit_Factorial(6), 0)
        self.assertEqual(last_Digit_Factorial(7), 0)
        # Add more tests if needed
