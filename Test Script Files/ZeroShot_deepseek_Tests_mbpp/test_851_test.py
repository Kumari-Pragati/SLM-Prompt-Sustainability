import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSumOfInverseDivisors(unittest.TestCase):

    def test_sum_of_inverse_divisors(self):
        self.assertEqual(Sum_of_Inverse_Divisors(5, 10), 2.0)
        self.assertEqual(Sum_of_Inverse_Divisors(3, 6), 4.0)
        self.assertEqual(Sum_of_Inverse_Divisors(2, 4), 2.0)
        self.assertEqual(Sum_of_Inverse_Divisors(1, 1), 1.0)
        self.assertEqual(Sum_of_Inverse_Divisors(0, 0), 0.0)
