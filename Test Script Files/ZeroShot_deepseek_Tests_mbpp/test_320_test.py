import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):

    def test_sum_difference_positive(self):
        self.assertEqual(sum_difference(10), 2640)

    def test_sum_difference_negative(self):
        self.assertEqual(sum_difference(-10), 0)

    def test_sum_difference_zero(self):
        self.assertEqual(sum_difference(0), 0)

    def test_sum_difference_large_number(self):
        self.assertEqual(sum_difference(100), 25164150)
