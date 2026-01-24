import unittest
from mbpp_893_code import Extract

class TestExtract(unittest.TestCase):

    def test_empty_list(self):
        """Test extract on an empty list"""
        self.assertListEqual(Extract([]), [])

    def test_single_item_list(self):
        """Test extract on a list with one item"""
        self.assertListEqual(Extract([[1]]), [1])

    def test_multiple_items_list(self):
        """Test extract on a list with multiple items"""
        self.assertListEqual(Extract([[1], [2], [3]]), [3, 2, 1])

    def test_list_with_non_list_items(self):
        """Test extract on a list with non-list items"""
        self.assertRaises(TypeError, Extract, [[1, 2], "test", 3])

    def test_list_with_empty_sublists(self):
        """Test extract on a list with empty sublists"""
        self.assertListEqual(Extract([[], [1], [2, 3]]), [2, 3])

    def test_list_with_negative_index(self):
        """Test extract on a list with negative index"""
        self.assertRaises(IndexError, Extract, [[1, 2], [-1]])
