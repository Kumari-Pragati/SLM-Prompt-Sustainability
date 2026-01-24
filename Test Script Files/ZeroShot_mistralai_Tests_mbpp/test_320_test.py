import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):

    def test_sum_difference_for_small_numbers(self):
        self.assertEqual(sum_difference(1), 0)
        self.assertEqual(sum_difference(2), 3)
        self.assertEqual(sum_difference(3), 10)
        self.assertEqual(sum_difference(4), 25)
        self.assertEqual(sum_difference(5), 42)

    def test_sum_difference_for_large_numbers(self):
        self.assertEqual(sum_difference(10), 225)
        self.assertEqual(sum_difference(100), 255025)
        self.assertEqual(sum_difference(1000), 24801625)
        self.assertEqual(sum_difference(10000), 2480162500)
        self.assertEqual(sum_difference(100000), 2480162500000)
