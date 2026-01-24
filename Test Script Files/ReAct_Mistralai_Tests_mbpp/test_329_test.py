import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):

    def test_empty_list(self):
        """Test that an empty list returns 0"""
        self.assertEqual(neg_count([]), 0)

    def test_positive_numbers(self):
        """Test that only negative numbers are counted"""
        self.assertEqual(neg_count([1, 2, -3, 4, -5]), 2)

    def test_negative_zero(self):
        """Test that -0 is counted as negative"""
        self.assertEqual(neg_count([-0, 2, -3]), 2)

    def test_single_negative_number(self):
        """Test that a single negative number is counted correctly"""
        self.assertEqual(neg_count([-1]), 1)

    def test_large_negative_numbers(self):
        """Test that large negative numbers are counted correctly"""
        self.assertEqual(neg_count([-1000000, -2000000]), 2)

    def test_floating_point_numbers(self):
        """Test that floating point numbers are counted correctly"""
        self.assertEqual(neg_count([-3.14, 2.71, -4.14]), 2)

    def test_list_of_zeros(self):
        """Test that a list of zeros returns 0"""
        self.assertEqual(neg_count([0, 0, 0]), 0)

    def test_list_of_ones(self):
        """Test that a list of ones returns 0"""
        self.assertEqual(neg_count([1, 1, 1]), 0)

    def test_list_of_positive_numbers(self):
        """Test that a list of positive numbers returns 0"""
        self.assertEqual(neg_count([1, 2, 3, 4, 5]), 0)

    def test_list_of_mixed_numbers(self):
        """Test that a list of mixed numbers is handled correctly"""
        self.assertEqual(neg_count([1, -2, 3, -4, 5]), 2)
