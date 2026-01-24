import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):

    def test_empty_list(self):
        """Test if the function returns the correct value for an empty list"""
        self.assertEqual(maximum_Sum([]), 0)

    def test_single_element_list(self):
        """Test if the function returns the correct value for a list with one element"""
        self.assertEqual(maximum_Sum([[1]]), 1)

    def test_single_integer_list(self):
        """Test if the function returns the correct value for a list with one integer"""
        self.assertEqual(maximum_Sum([1]), 1)

    def test_positive_numbers_list(self):
        """Test if the function returns the correct value for a list with positive numbers"""
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 24)

    def test_negative_numbers_list(self):
        """Test if the function returns the correct value for a list with negative numbers"""
        self.assertEqual(maximum_Sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), 24)

    def test_mixed_numbers_list(self):
        """Test if the function returns the correct value for a list with mixed numbers"""
        self.assertEqual(maximum_Sum([[1, -2, 3], [-4, 5, 6], [7, -8, 9]]), 19)

    def test_list_with_zero(self):
        """Test if the function returns the correct value for a list with zero"""
        self.assertEqual(maximum_Sum([[0], [1, 2, 3], [-4, 0, 6], [7, 0, 9]]), 12)

    def test_list_with_large_numbers(self):
        """Test if the function returns the correct value for a list with large numbers"""
        self.assertEqual(maximum_Sum([[1000000001, 2, 3], [4, 500000006, 6], [7, 800000009, 9]]), 1000000009)

    def test_list_with_negative_large_numbers(self):
        """Test if the function returns the correct value for a list with negative large numbers"""
        self.assertEqual(maximum_Sum([[-1000000001, -2, -3], [-4, -500000006, -6], [-7, -800000009, -9]]), -999999998)
