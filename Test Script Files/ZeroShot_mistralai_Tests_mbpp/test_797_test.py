import unittest
from797_code import sum_in_Range, sum_Odd

class TestSumInRange(unittest.TestCase):

    def test_sum_in_range_positive(self):
        self.assertEqual(sum_in_Range(1, 5), 8)
        self.assertEqual(sum_in_Range(5, 10), 25)
        self.assertEqual(sum_in_Range(10, 20), 90)

    def test_sum_in_range_negative(self):
        self.assertEqual(sum_in_Range(-5, 0), 0)
        self.assertEqual(sum_in_Range(-10, -5), 20)
        self.assertEqual(sum_in_Range(-20, -10), 175)

    def test_sum_in_range_zero(self):
        self.assertEqual(sum_in_Range(0, 0), 0)

    def test_sum_in_range_one(self):
        self.assertEqual(sum_in_Range(1, 1), 1)

    def test_sum_in_range_large(self):
        self.assertEqual(sum_in_Range(1000000, 1000005), 2500001)
