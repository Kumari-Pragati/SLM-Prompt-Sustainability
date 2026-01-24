import unittest
from mbpp_849_code import Sum

class TestSumFunction(unittest.TestCase):

    def test_sum_of_prime_divisors(self):
        self.assertEqual(Sum(1), 0)
        self.assertEqual(Sum(2), 2)
        self.assertEqual(Sum(3), 3)
        self.assertEqual(Sum(4), 2)
        self.assertEqual(Sum(5), 5)
        self.assertEqual(Sum(6), 3)
        self.assertEqual(Sum(7), 7)
        self.assertEqual(Sum(8), 3)
        self.assertEqual(Sum(9), 3)
        self.assertEqual(Sum(10), 4)
        self.assertEqual(Sum(12), 7)
        self.assertEqual(Sum(15), 13)
        self.assertEqual(Sum(20), 14)
        self.assertEqual(Sum(25), 17)
        self.assertEqual(Sum(30), 19)
        self.assertEqual(Sum(40), 28)
        self.assertEqual(Sum(50), 31)
        self.assertEqual(Sum(60), 37)
        self.assertEqual(Sum(70), 43)
        self.assertEqual(Sum(80), 49)
        self.assertEqual(Sum(90), 55)
        self.assertEqual(Sum(100), 64)
