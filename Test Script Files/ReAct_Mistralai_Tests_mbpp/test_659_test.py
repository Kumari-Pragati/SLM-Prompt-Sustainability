import unittest
from mbpp_659_code import Repeat

class TestRepeatFunction(unittest.TestCase):

    def test_empty_list(self):
        """Test function behavior with an empty list"""
        self.assertListEqual(Repeat([]), [])

    def test_single_element_list(self):
        """Test function behavior with a list containing a single element"""
        self.assertListEqual(Repeat([1]), [1])

    def test_duplicate_elements(self):
        """Test function behavior with a list containing duplicate elements"""
        self.assertListEqual(Repeat([1, 1, 2, 2, 3]), [1, 2])

    def test_single_duplicate_element(self):
        """Test function behavior with a list containing a single duplicate element"""
        self.assertListEqual(Repeat([1, 1]), [1])

    def test_no_duplicates(self):
        """Test function behavior with a list containing no duplicates"""
        self.assertListEqual(Repeat([1, 2, 3]), [])

    def test_list_with_only_duplicates(self):
        """Test function behavior with a list containing only duplicates"""
        self.assertListEqual(Repeat([1, 1, 1]), [1])

    def test_negative_index(self):
        """Test function behavior with negative indices"""
        with self.assertRaises(IndexError):
            Repeat([1, 2], -1)

    def test_zero_index(self):
        """Test function behavior with zero index"""
        self.assertListEqual(Repeat([1, 2]), [1])

    def test_large_input(self):
        """Test function behavior with a large input list"""
        self.assertListEqual(Repeat([1] * 1000), [1])
