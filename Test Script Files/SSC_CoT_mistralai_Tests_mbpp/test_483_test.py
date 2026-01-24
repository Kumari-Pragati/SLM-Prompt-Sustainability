import unittest
from mbpp_483_code import first_Factorial_DivisibleNumber

class TestFirstFactorialDivisibleNumber(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(first_Factorial_DivisibleNumber(5), 12)
        self.assertEqual(first_Factorial_DivisibleNumber(10), 24)
        self.assertEqual(first_Factorial_DivisibleNumber(15), 120)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(first_Factorial_DivisibleNumber(0), 1)
        self.assertEqual(first_Factorial_DivisibleNumber(1), 1)
        self.assertEqual(first_Factorial_DivisibleNumber(2), 2)
        self.assertEqual(first_Factorial_DivisibleNumber(3), 6)
        self.assertEqual(first_Factorial_DivisibleNumber(4), 24)
        self.assertEqual(first_Factorial_DivisibleNumber(6), 720)
        self.assertEqual(first_Factorial_DivisibleNumber(7), 5040)
        self.assertEqual(first_Factorial_DivisibleNumber(8), 40320)

    def test_special_cases(self):
        self.assertEqual(first_Factorial_DivisibleNumber(9), 3628800)
        self.assertEqual(first_Factorial_DivisibleNumber(12), 479001600)
        self.assertEqual(first_Factorial_DivisibleNumber(14), 87178291200)
        self.assertEqual(first_Factorial_DivisibleNumber(18), 6402373705728000)
