import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):

    def test_empty_list(self):
        """Test zero_count with an empty list"""
        self.assertAlmostEqual(zero_count([]), 0.00)

    def test_single_zero(self):
        """Test zero_count with a list containing a single zero"""
        self.assertAlmostEqual(zero_count([0]), 1.00)

    def test_multiple_zeros(self):
        """Test zero_count with a list containing multiple zeros"""
        self.assertAlmostEqual(zero_count([0, 0, 0, 1, 2, 0]), 3.00)

    def test_all_zeros(self):
        """Test zero_count with a list containing only zeros"""
        self.assertAlmostEqual(zero_count([0] * 100), 1.00)

    def test_all_non_zeros(self):
        """Test zero_count with a list containing only non-zeros"""
        self.assertAlmostEqual(zero_count([1, 2, 3, 4, 5]), 0.00)

    def test_negative_numbers(self):
        """Test zero_count with a list containing negative numbers"""
        self.assertAlmostEqual(zero_count([-1, 0, 1]), 0.50)

    def test_large_list(self):
        """Test zero_count with a large list to ensure performance is acceptable"""
        large_list = [0] * 10000
        self.assertAlmostEqual(zero_count(large_list), 1.00)
