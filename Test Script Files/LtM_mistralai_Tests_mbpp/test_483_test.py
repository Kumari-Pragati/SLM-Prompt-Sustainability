import unittest
from mbpp_483_code import first_Factorial_Divisible_Number

class TestFirstFactorialDivisibleNumber(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(first_Factorial_DivisibleNumber(3), 6)

    def test_edge_case_small(self):
        self.assertEqual(first_Factorial_DivisibleNumber(1), 1)

    def test_edge_case_large(self):
        self.assertEqual(first_Factorial_DivisibleNumber(100), 243160)

    def test_boundary_case_zero(self):
        self.assertRaises(ValueError, first_Factorial_DivisibleNumber, 0)

    def test_boundary_case_negative(self):
        self.assertRaises(ValueError, first_Factorial_DivisibleNumber, -1)

    def test_complex_case(self):
        self.assertEqual(first_Factorial_DivisibleNumber(4), 10)
