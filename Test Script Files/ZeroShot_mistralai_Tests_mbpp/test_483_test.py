import unittest
from mbpp_483_code import first_Factorial_Divisible_Number

class TestFirstFactorialDivisibleNumber(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(first_Factorial_DivisibleNumber(0), None)

    def test_one(self):
        self.assertEqual(first_Factorial_DivisibleNumber(1), 1)

    def test_two(self):
        self.assertEqual(first_Factorial_DivisibleNumber(2), 2)

    def test_three(self):
        self.assertEqual(first_Factorial_DivisibleNumber(3), 6)

    def test_four(self):
        self.assertEqual(first_Factorial_DivisibleNumber(4), 24)

    def test_five(self):
        self.assertEqual(first_Factorial_DivisibleNumber(5), 120)

    def test_negative_number(self):
        self.assertRaises(ValueError, first_Factorial_DivisibleNumber, -1)

    def test_large_number(self):
        self.assertEqual(first_Factorial_DivisibleNumber(100), 3628800)
