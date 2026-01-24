import unittest
from mbpp_483_code import first_Factorial_Divisible_Number

class TestFirstFactorialDivisibleNumber(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(first_Factorial_Divisible_Number(1), 1)
        self.assertEqual(first_Factorial_Divisible_Number(2), 2)
        self.assertEqual(first_Factorial_Divisible_Number(3), 6)
        self.assertEqual(first_Factorial_Divisible_Number(4), 2)
        self.assertEqual(first_Factorial_Divisible_Number(5), 120)

    def test_zero_and_negative_numbers(self):
        self.assertEqual(first_Factorial_Divisible_Number(0), 0)
        self.assertEqual(first_Factorial_Divisible_Number(-1), 1)

    def test_large_numbers(self):
        self.assertEqual(first_Factorial_Divisible_Number(10), 10)
        self.assertEqual(first_Factorial_Divisible_Number(20), 20)
