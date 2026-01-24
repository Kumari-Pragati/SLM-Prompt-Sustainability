import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):

    def test_sum_of_prime_numbers(self):
        self.assertEqual(Sum(2), 2)
        self.assertEqual(Sum(3), 3)
        self.assertEqual(Sum(5), 5)
        self.assertEqual(Sum(7), 7)
        self.assertEqual(Sum(11), 11)

    def test_sum_of_composite_numbers(self):
        self.assertEqual(Sum(4), 3)
        self.assertEqual(Sum(6), 5)
        self.assertEqual(Sum(8), 3)
        self.assertEqual(Sum(9), 5)
        self.assertEqual(Sum(10), 4)
        self.assertEqual(Sum(12), 7)
        self.assertEqual(Sum(13), 13)

    def test_sum_of_large_numbers(self):
        self.assertEqual(Sum(100), 25164150)
        self.assertEqual(Sum(1000), 2341658335)

    def test_sum_of_small_numbers(self):
        self.assertEqual(Sum(0), 0)
        self.assertEqual(Sum(1), 0)

    def test_sum_of_negative_numbers(self):
        with self.assertRaises(ValueError):
            Sum(-1)
