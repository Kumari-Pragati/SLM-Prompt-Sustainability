import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):

    def test_empty_list(self):
        """Test empty list"""
        self.assertEqual(trim_tuple([], 0), "[]")

    def test_single_element_list(self):
        """Test single element list"""
        self.assertEqual(trim_tuple([(1, 2, 3)], 1), "[(2, 3)]")

    def test_multi_element_list(self):
        """Test multiple elements list"""
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 1), "[(2, 3), (5, 6), (8, 9)]")

    def test_list_with_different_lengths(self):
        """Test list with different lengths"""
        self.assertEqual(trim_tuple([(1, 2, 3), (4), (7, 8, 9, 10)], 1), "[(2, 3), (4), (8, 9)]")

    def test_list_with_negative_k(self):
        """Test list with negative K"""
        with self.assertRaises(ValueError):
            trim_tuple([(1, 2, 3)], -1)

    def test_list_with_k_greater_than_length(self):
        """Test list with K greater than length"""
        with self.assertRaises(ValueError):
            trim_tuple([(1, 2, 3)], 4)
