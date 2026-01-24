import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):

    def test_positive_integer(self):
        """Test series_sum with positive integer"""
        self.assertEqual(series_sum(1), 1)
        self.assertEqual(series_sum(2), 9/2)
        self.assertEqual(series_sum(5), 1215/60)

    def test_zero(self):
        """Test series_sum with zero"""
        self.assertEqual(series_sum(0), 0)

    def test_negative_integer(self):
        """Test series_sum with negative integer"""
        self.assertEqual(series_sum(-1), -1/6)
        self.assertEqual(series_sum(-2), -13/6)
        self.assertEqual(series_sum(-5), -1215/60)

    def test_large_integer(self):
        """Test series_sum with large integer"""
        self.assertEqual(series_sum(100), 335503360/3003)
        self.assertEqual(series_sum(1000), 16796025900/94503003)

    def test_floating_point(self):
        """Test series_sum with floating point number"""
        self.assertAlmostEqual(series_sum(2.5), 265/12)
        self.assertAlmostEqual(series_sum(3.5), 133/6)
