import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):

    def test_empty_list(self):
        """Test if an empty list returns an empty list"""
        self.assertListEqual(diff_consecutivenums([]), [])

    def test_single_element_list(self):
        """Test if a single-element list returns an empty list"""
        self.assertListEqual(diff_consecutivenums([1]), [])

    def test_consecutive_numbers(self):
        """Test if consecutive numbers are correctly subtracted"""
        self.assertListEqual(diff_consecutivenums([1, 2, 3, 4, 5]), [1, 1, 1])

    def test_negative_numbers(self):
        """Test if negative numbers are correctly subtracted"""
        self.assertListEqual(diff_consecutivenums([-1, -2, -3, -4, -5]), [1, 1, 1, 1])

    def test_mixed_numbers(self):
        """Test if mixed positive and negative numbers are correctly subtracted"""
        self.assertListEqual(diff_consecutivenums([1, -2, 3, -4, 5]), [1, 3, 1, -1])

    def test_zero_in_list(self):
        """Test if zero is correctly skipped"""
        self.assertListEqual(diff_consecutivenums([1, 0, 2, 0, 3]), [1, 2, 0])

    def test_list_with_one_zero(self):
        """Test if a list with one zero returns an empty list"""
        self.assertListEqual(diff_consecutivenums([0, 1, 2, 3]), [])

    def test_list_with_multiple_zeros(self):
        """Test if a list with multiple zeros returns an empty list"""
        self.assertListEqual(diff_consecutivenums([0, 1, 0, 2, 0, 3]), [])
