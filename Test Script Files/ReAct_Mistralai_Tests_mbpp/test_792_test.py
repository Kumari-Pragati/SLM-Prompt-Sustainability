import unittest
from mbpp_792_code import count_list

class TestCountList(unittest.TestCase):

    def test_empty_list(self):
        """Test that an empty list returns a count of 0"""
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        """Test that a list with one element returns a count of 1"""
        self.assertEqual(count_list([1]), 1)

    def test_multiple_elements_list(self):
        """Test that a list with multiple elements returns the correct count"""
        self.assertEqual(count_list([1, 2, 3]), 3)

    def test_list_with_duplicates(self):
        """Test that a list with duplicates returns the correct count"""
        self.assertEqual(count_list([1, 1, 2, 2, 3]), 5)

    def test_list_with_negative_numbers(self):
        """Test that a list with negative numbers returns the correct count"""
        self.assertEqual(count_list([-1, 0, 1]), 3)

    def test_list_with_mixed_types(self):
        """Test that a list with mixed types returns the correct count (ignores non-numbers)"""
        self.assertEqual(count_list([1, 'a', 2, None, 3.0]), 4)

    def test_list_with_large_numbers(self):
        """Test that a list with large numbers returns the correct count"""
        self.assertEqual(count_list([1000000001, 1000000002, 1000000003]), 3)

    def test_list_with_very_large_numbers(self):
        """Test that a list with very large numbers returns the correct count"""
        self.assertEqual(count_list([sys.maxsize, sys.maxsize + 1, sys.maxsize + 2]), 3)
