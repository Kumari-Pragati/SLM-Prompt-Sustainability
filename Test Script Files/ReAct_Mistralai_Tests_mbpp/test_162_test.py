import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_zero(self):
        """Test sum_series with n=0"""
        self.assertEqual(sum_series(0), 0)

    def test_negative(self):
        """Test sum_series with negative n"""
        self.assertEqual(sum_series(-1), 0)

    def test_one(self):
        """Test sum_series with n=1"""
        self.assertEqual(sum_series(1), 1)

    def test_two(self):
        """Test sum_series with n=2"""
        self.assertEqual(sum_series(2), 3)

    def test_large_positive(self):
        """Test sum_series with large positive n"""
        self.assertEqual(sum_series(100), 9999)

    def test_large_negative(self):
        """Test sum_series with large negative n"""
        self.assertEqual(sum_series(-100), 9999)

    def test_odd_large(self):
        """Test sum_series with odd large n"""
        self.assertEqual(sum_series(101), 9999 + 101)

    def test_even_large(self):
        """Test sum_series with even large n"""
        self.assertEqual(sum_series(100), 9999)
