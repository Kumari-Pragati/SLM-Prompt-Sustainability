import unittest
from mbpp_483_code import first_Factorial_Divisible_Number

class TestFirstFactorialDivisibleNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_Factorial_Divisible_Number(5), 4)

    def test_edge_case(self):
        self.assertEqual(first_Factorial_Divisible_Number(1), 1)

    def test_boundary_case(self):
        self.assertEqual(first_Factorial_Divisible_Number(2), 1)

    def test_corner_case(self):
        self.assertEqual(first_Factorial_Divisible_Number(3), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            first_Factorial_Divisible_Number('a')
