import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):

    def test_empty_list(self):
        """Test if the function returns correct value for empty list"""
        self.assertIs(largest_neg([]), float('-inf'))

    def test_single_element_list(self):
        """Test if the function returns correct value for a single element list"""
        for num in [-1, 0, 1]:
            self.assertEqual(largest_neg([num]), num)

    def test_positive_list(self):
        """Test if the function returns correct value for a list containing only positive numbers"""
        self.assertIs(largest_neg([1, 2, 3]), -float('inf'))

    def test_negative_list(self):
        """Test if the function returns correct value for a list containing only negative numbers"""
        self.assertIs(largest_neg([-1, -2, -3]), -3)

    def test_mixed_list(self):
        """Test if the function returns correct value for a list containing both positive and negative numbers"""
        self.assertIs(largest_neg([-1, 0, 1, -2, 3]), -2)

    def test_list_with_zero(self):
        """Test if the function returns correct value for a list containing zero"""
        self.assertIs(largest_neg([0, -1, 1]), -1)

    def test_list_with_inf(self):
        """Test if the function returns correct value for a list containing inf"""
        self.assertIs(largest_neg([-1, float('inf')]), -1)

    def test_list_with_nan(self):
        """Test if the function returns correct value for a list containing nan"""
        self.assertIs(largest_neg([-1, float('nan')]), -1)
