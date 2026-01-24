import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSumOfInverseDivisors(unittest.TestCase):

    def test_sum_of_inverse_divisors(self):
        self.assertEqual(Sum_of_Inverse_Divisors(2, 1), 1.0)
        self.assertEqual(Sum_of_Inverse_Divisors(4, 1.5), 1.5)
        self.assertEqual(Sum_of_Inverse_Divisors(8, 1.125), 1.125)
        self.assertEqual(Sum_of_Inverse_Divisors(10, 1.4), 1.4)
        self.assertEqual(Sum_of_Inverse_Divisors(20, 2.0), 2.0)
        self.assertEqual(Sum_of_Inverse_Divisors(25, 1.6), 1.6)
        self.assertEqual(Sum_of_Inverse_Divisors(100, 10.0), 10.0)
        self.assertEqual(Sum_of_Inverse_Divisors(24, 1.5), 1.5)
        self.assertEqual(Sum_of_Inverse_Divisors(496, 9.9), 9.9)
