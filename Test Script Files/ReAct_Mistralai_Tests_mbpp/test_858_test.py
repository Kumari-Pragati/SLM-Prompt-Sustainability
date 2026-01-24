import unittest
from mbpp_858_code import count_list

class TestCountList(unittest.TestCase):

    def test_empty_list(self):
        """Test that an empty list returns 0"""
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        """Test that a list with one element returns 1"""
        self.assertEqual(count_list([1]), 1)

    def test_multiple_elements_list(self):
        """Test that a list with multiple elements returns the correct square"""
        self.assertEqual(count_list([1, 2, 3]), 16)

    def test_negative_numbers_list(self):
        """Test that a list with negative numbers returns the correct square"""
        self.assertEqual(count_list([-1, -2, -3]), 16)

    def test_mixed_numbers_list(self):
        """Test that a list with mixed numbers returns the correct square"""
        self.assertEqual(count_list([1, -2, 3, -4]), 49)

    def test_list_with_duplicates(self):
        """Test that a list with duplicates returns the correct square"""
        self.assertEqual(count_list([1, 1, 2, 2, 3, 3]), 36)

    def test_large_list(self):
        """Test that a large list returns the correct square"""
        large_list = [i for i in range(100)]
        self.assertEqual(count_list(large_list), 10000)

    def test_list_with_non_numeric_elements(self):
        """Test that a list with non-numeric elements raises a ValueError"""
        self.assertRaises(ValueError, count_list, ['a', 1, 'b'])
