import unittest
from mbpp_483_code import first_Factorial_DivisibleNumber

class TestFirstFactorialDivisibleNumber(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(first_Factorial_DivisibleNumber(3), 6)
        self.assertEqual(first_Factorial_DivisibleNumber(5), 120)
        self.assertEqual(first_Factorial_DivisibleNumber(10), 3628800)

    def test_zero(self):
        self.assertRaises(ValueError, first_Factorial_DivisibleNumber, 0)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, first_Factorial_DivisibleNumber, -1)
        self.assertRaises(ValueError, first_Factorial_DivisibleNumber, -2)

    def test_one(self):
        self.assertEqual(first_Factorial_DivisibleNumber(1), 1)

    def test_large_numbers(self):
        self.assertEqual(first_Factorial_DivisibleNumber(1000), 30414093201713378043612608166064768844377641568960512000000)

    def test_small_factors(self):
        self.assertEqual(first_Factorial_DivisibleNumber(2), 2)
        self.assertEqual(first_Factorial_DivisibleNumber(7), 5040)
