import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):

    def test_positive_integer(self):
        """Test sum_difference with positive integers"""
        for n in [1, 2, 5, 10, 100]:
            result = sum_difference(n)
            self.assertAlmostEqual(result, (n * (n + 1) * (2 * n + 1)) // 6)

    def test_zero(self):
        """Test sum_difference with zero"""
        result = sum_difference(0)
        self.assertEqual(result, 0)

    def test_negative_integer(self):
        """Test sum_difference with negative integers"""
        for n in [-1, -2, -5, -10, -100]:
            result = sum_difference(abs(n))
            self.assertAlmostEqual(result, (-n * (n + 1) * (2 * n + 1)) // 6)

    def test_large_integer(self):
        """Test sum_difference with large integers"""
        result = sum_difference(100000)
        self.assertGreater(result, 1e12)
