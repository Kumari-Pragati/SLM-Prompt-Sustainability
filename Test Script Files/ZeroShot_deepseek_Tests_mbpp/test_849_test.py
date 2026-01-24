import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):

    def test_sum_of_prime_divisors(self):
        self.assertEqual(Sum(1), 0)
        self.assertEqual(Sum(2), 2)
        self.assertEqual(Sum(3), 3)
        self.assertEqual(Sum(4), 4)
        self.assertEqual(Sum(5), 5)
        self.assertEqual(Sum(6), 6)
        self.assertEqual(Sum(7), 7)
        self.assertEqual(Sum(8), 7)
        self.assertEqual(Sum(9), 3)
        self.assertEqual(Sum(10), 8)
        self.assertEqual(Sum(11), 11)
        self.assertEqual(Sum(12), 10)
        self.assertEqual(Sum(13), 13)
        self.assertEqual(Sum(14), 11)
        self.assertEqual(Sum(15), 8)
        self.assertEqual(Sum(16), 11)
        self.assertEqual(Sum(17), 17)
        self.assertEqual(Sum(18), 12)
        self.assertEqual(Sum(19), 19)
        self.assertEqual(Sum(20), 14)
