import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertAlmostEqual(negative_count([]), 0.00)

    def test_all_positive(self):
        """Test with a list of all positive numbers"""
        self.assertAlmostEqual(negative_count([1, 2, 3, 4, 5]), 0.00)

    def test_all_negative(self):
        """Test with a list of all negative numbers"""
        self.assertAlmostEqual(negative_count([-1, -2, -3, -4, -5]), 1.00)

    def test_mixed_positive_and_negative(self):
        """Test with a mixed list of positive and negative numbers"""
        self.assertAlmostEqual(negative_count([-1, 1, -2, 2, -3, 3]), 0.50)

    def test_zero(self):
        """Test with a zero"""
        self.assertAlmostEqual(negative_count([0]), 0.00)

    def test_large_positive_numbers(self):
        """Test with large positive numbers"""
        self.assertAlmostEqual(negative_count([1000000, 2000000, 3000000]), 0.00)

    def test_large_negative_numbers(self):
        """Test with large negative numbers"""
        self.assertAlmostEqual(negative_count([-1000000, -2000000, -3000000]), 1.00)

    def test_floating_point_numbers(self):
        """Test with floating point numbers"""
        self.assertAlmostEqual(negative_count([-3.14, 2.71, -1.618]), 0.50)
