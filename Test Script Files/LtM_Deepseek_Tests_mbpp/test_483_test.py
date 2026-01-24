import unittest
from mbpp_483_code import first_Factorial_Divisible_Number

class TestFirstFactorialDivisibleNumber(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(first_Factorial_Divisible_Number(1), 1)
        self.assertEqual(first_Factorial_Divisible_Number(2), 2)
        self.assertEqual(first_Factorial_Divisible_Number(3), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(first_Factorial_Divisible_Number(0), 1)
        self.assertEqual(first_Factorial_Divisible_Number(40), 2)

    def test_more_complex_or_corner_cases(self):
        self.assertEqual(first_Factorial_Divisible_Number(10), 2)
        self.assertEqual(first_Factorial_Divisible_Number(15), 6)
