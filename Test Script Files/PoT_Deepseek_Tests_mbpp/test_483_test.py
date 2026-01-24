import unittest
from mbpp_483_code import first_Factorial_Divisible_Number

class TestFirstFactorialDivisibleNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(first_Factorial_Divisible_Number(1), 1)
        self.assertEqual(first_Factorial_Divisible_Number(2), 2)
        self.assertEqual(first_Factorial_Divisible_Number(3), 6)
        self.assertEqual(first_Factorial_Divisible_Number(4), 6)
        self.assertEqual(first_Factorial_Divisible_Number(5), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(first_Factorial_Divisible_Number(0), 1)
        self.assertEqual(first_Factorial_Divisible_Number(1), 1)

    def test_corner_cases(self):
        self.assertEqual(first_Factorial_Divisible_Number(6), 6)
        self.assertEqual(first_Factorial_Divisible_Number(7), 6)
        self.assertEqual(first_Factorial_Divisible_Number(8), 6)
        self.assertEqual(first_Factorial_Divisible_Number(9), 6)
        self.assertEqual(first_Factorial_Divisible_Number(10), 2520)
