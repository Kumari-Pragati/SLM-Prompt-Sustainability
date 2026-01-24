import unittest
from mbpp_483_code import first_Factorial_DivisibleNumber

class TestFirstFactorialDivisibleNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_Factorial_DivisibleNumber(3), 6)
        self.assertEqual(first_Factorial_DivisibleNumber(5), 120)
        self.assertEqual(first_Factorial_DivisibleNumber(7), 5040)

    def test_edge_case_small(self):
        self.assertEqual(first_Factorial_DivisibleNumber(1), 1)
        self.assertEqual(first_Factorial_DivisibleNumber(2), 2)

    def test_edge_case_large(self):
        self.assertEqual(first_Factorial_DivisibleNumber(100), 3628800)

    def test_boundary_case_zero(self):
        self.assertRaises(ValueError, first_Factorial_DivisibleNumber, 0)

    def test_boundary_case_negative(self):
        self.assertRaises(ValueError, first_Factorial_DivisibleNumber, -1)
