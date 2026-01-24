import unittest
from mbpp_629_code import Split

class TestSplitFunction(unittest.TestCase):

    def test_empty_list(self):
        """Test that an empty list returns an empty list"""
        self.assertListEqual(Split([]), [])

    def test_single_even_element(self):
        """Test that a single even number is correctly identified"""
        self.assertListEqual(Split([2]), [2])

    def test_single_odd_element(self):
        """Test that a single odd number is correctly ignored"""
        self.assertListEqual(Split([1]), [])

    def test_multiple_even_elements(self):
        """Test that multiple even numbers are correctly identified"""
        self.assertListEqual(Split([2, 4, 6]), [2, 4, 6])

    def test_multiple_odd_elements(self):
        """Test that multiple odd numbers are correctly ignored"""
        self.assertListEqual(Split([1, 3, 5]), [])

    def test_mixed_elements(self):
        """Test that mixed even and odd numbers are correctly identified"""
        self.assertListEqual(Split([1, 2, 3, 4, 5, 6]), [2, 4])

    def test_negative_numbers(self):
        """Test that negative numbers are correctly identified"""
        self.assertListEqual(Split([-2, -4, -6]), [-2, -4, -6])

    def test_zero(self):
        """Test that zero is correctly identified"""
        self.assertListEqual(Split([0]), [0])

    def test_large_numbers(self):
        """Test that large numbers are correctly identified"""
        self.assertListEqual(Split([10, 12, 14, 16]), [10, 12, 14])
