import unittest
from mbpp_483_code import first_Factorial_Divisible_Number

class TestFirstFactorialDivisibleNumber(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(first_Factorial_DivisibleNumber(4), 6)
        self.assertEqual(first_Factorial_DivisibleNumber(10), 24)
        self.assertEqual(first_Factorial_DivisibleNumber(20), 120)

    def test_zero(self):
        self.assertEqual(first_Factorial_DivisibleNumber(0), 1)

    def test_negative_number(self):
        self.assertEqual(first_Factorial_DivisibleNumber(-1), None)
        self.assertEqual(first_Factorial_DivisibleNumber(-2), None)

    def test_large_number(self):
        self.assertEqual(first_Factorial_DivisibleNumber(100), None)
