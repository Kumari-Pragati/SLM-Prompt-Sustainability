import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(sum_difference(5), 28.25)
        self.assertAlmostEqual(sum_difference(10), 208.33333333333336)

    def test_zero(self):
        self.assertEqual(sum_difference(0), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(sum_difference(-5), -28.25)

    def test_large_number(self):
        self.assertAlmostEqual(sum_difference(1000), 333333333.33333336)

    def test_small_number(self):
        self.assertAlmostEqual(sum_difference(1), 0.01)
