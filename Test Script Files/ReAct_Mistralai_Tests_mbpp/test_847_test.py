import unittest
from mbpp_847_code import lcopy

class TestLCopy(unittest.TestCase):

    def test_empty_list(self):
        """Test lcopy on an empty list"""
        result = lcopy([])
        self.assertListEqual(result, [])

    def test_single_element_list(self):
        """Test lcopy on a list with one element"""
        result = lcopy([42])
        self.assertListEqual(result, [42])

    def test_multiple_elements_list(self):
        """Test lcopy on a list with multiple elements"""
        result = lcopy([1, 2, 3, 4])
        self.assertListEqual(result, [1, 2, 3, 4])

    def test_list_with_duplicates(self):
        """Test lcopy on a list with duplicates"""
        result = lcopy([1, 2, 2, 3, 4, 4, 4])
        self.assertListEqual(result, [1, 2, 2, 3, 4, 4, 4])

    def test_list_with_negative_index(self):
        """Test lcopy on a list with negative index"""
        result = lcopy([-1, -2, -3])
        self.assertListEqual(result, [-1, -2, -3])

    def test_list_with_large_positive_index(self):
        """Test lcopy on a list with large positive index"""
        result = lcopy([0, 1, 2, 3, 4] * 10000)
        self.assertListEqual(result, [0] * 10000 + [1] * 10000 + [2] * 10000 + [3] * 10000 + [4] * 10000)

    def test_list_with_large_negative_index(self):
        """Test lcopy on a list with large negative index"""
        result = lcopy([0, 1, 2, 3, 4] * 10000)
        self.assertListEqual(result, [0] * 10000 + [1] * 10000 + [2] * 10000 + [3] * 10000 + [4] * 10000)

    def test_list_with_non_list_input(self):
        """Test lcopy with non-list input"""
        with self.assertRaises(TypeError):
            lcopy(42)
