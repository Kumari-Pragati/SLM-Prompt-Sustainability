import unittest
from mbpp_483_code import first_Factorial_Divisible_Number

class TestFirstFactorialDivisibleNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(first_Factorial_Divisible_Number(1), 1)
        self.assertEqual(first_Factorial_Divisible_Number(2), 1)
        self.assertEqual(first_Factorial_Divisible_Number(3), 2)
        self.assertEqual(first_Factorial_Divisible_Number(4), 2)
        self.assertEqual(first_Factorial_Divisible_Number(5), 4)

    def test_edge_cases(self):
        self.assertEqual(first_Factorial_Divisible_Number(0), 0)
        self.assertEqual(first_Factorial_Divisible_Number(10), 8)
        self.assertEqual(first_Factorial_Divisible_Number(20), 18)

    def test_explicitly_handled_error_cases(self):
        self.assertRaises(ValueError, first_Factorial_Divisible_Number, -1)
        self.assertRaises(ValueError, first_Factorial_Divisible_Number, 'a')
