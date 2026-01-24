import unittest
from mbpp_483_code import first_Factorial_Divisible_Number

class TestFirstFactorialDivisibleNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_Factorial_Divisible_Number(10), 9)

    def test_edge_case(self):
        self.assertEqual(first_Factorial_Divisible_Number(1), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            first_Factorial_Divisible_Number('a')

        with self.assertRaises(ValueError):
            first_Factorial_Divisible_Number(-1)
