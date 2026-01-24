import unittest
from mbpp_483_code import first_Factorial_Divisible_Number

class TestFirstFactorialDivisibleNumber(unittest.TestCase):

    def test_first_Factorial_Divisible_Number(self):
        self.assertEqual(first_Factorial_Divisible_Number(1), 1)
        self.assertEqual(first_Factorial_Divisible_Number(2), 1)
        self.assertEqual(first_Factorial_Divisible_Number(3), 2)
        self.assertEqual(first_Factorial_Divisible_Number(4), 2)
        self.assertEqual(first_Factorial_Divisible_Number(5), 4)
        self.assertEqual(first_Factorial_Divisible_Number(6), 4)
        self.assertEqual(first_Factorial_Divisible_Number(7), 6)
        self.assertEqual(first_Factorial_Divisible_Number(8), 6)
        self.assertEqual(first_Factorial_Divisible_Number(9), 8)
        self.assertEqual(first_Factorial_Divisible_Number(10), 8)
        self.assertEqual(first_Factorial_Divisible_Number(11), 11)
        self.assertEqual(first_Factorial_Divisible_Number(12), 11)
        self.assertEqual(first_Factorial_Divisible_Number(13), 12)
        self.assertEqual(first_Factorial_Divisible_Number(14), 12)
        self.assertEqual(first_Factorial_Divisible_Number(15), 15)
        self.assertEqual(first_Factorial_Divisible_Number(16), 15)
        self.assertEqual(first_Factorial_Divisible_Number(17), 17)
        self.assertEqual(first_Factorial_Divisible_Number(18), 17)
        self.assertEqual(first_Factorial_Divisible_Number(19), 19)
        self.assertEqual(first_Factorial_Divisible_Number(20), 19)
