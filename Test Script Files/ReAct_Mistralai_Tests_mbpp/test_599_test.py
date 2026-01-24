import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):

    def test_sum_average_positive_integer(self):
        """Test sum_average with a positive integer"""
        result = sum_average(5)
        self.assertEqual(result[0], 15)
        self.assertAlmostEqual(result[1], 3.0)

    def test_sum_average_zero(self):
        """Test sum_average with zero"""
        result = sum_average(0)
        self.assertEqual(result, (0, float('nan')))

    def test_sum_average_negative_integer(self):
        """Test sum_average with a negative integer"""
        result = sum_average(-5)
        self.assertEqual(result[0], -5)
        self.assertAlmostEqual(result[1], -1.0)

    def test_sum_average_large_integer(self):
        """Test sum_average with a large integer"""
        result = sum_average(100000)
        self.assertGreater(result[0], 4999950000)
        self.assertAlmostEqual(result[1], 499995.0)
