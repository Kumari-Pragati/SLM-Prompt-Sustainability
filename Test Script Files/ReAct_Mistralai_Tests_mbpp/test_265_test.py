import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):

    def test_empty_list(self):
        """Test splitting an empty list"""
        self.assertListEqual(list_split([], 3), [[]])

    def test_single_element(self):
        """Test splitting a list with one element"""
        self.assertListEqual(list_split([1], 1), [ [1] ])
        self.assertListEqual(list_split([1], 2), [ [1] ])
        self.assertListEqual(list_split([1], 3), [ [1] ])

    def test_simple_list(self):
        """Test splitting a simple list"""
        self.assertListEqual(list_split([1, 2, 3, 4], 1), [ [1], [2], [3], [4] ])
        self.assertListEqual(list_split([1, 2, 3, 4], 2), [ [1, 2], [3, 4] ])
        self.assertListEqual(list_split([1, 2, 3, 4], 3), [ [1, 2, 3], [4] ])
        self.assertListEqual(list_split([1, 2, 3, 4], 4), [ [1, 2, 3, 4] ])

    def test_negative_step(self):
        """Test splitting with a negative step"""
        with self.assertRaises(ValueError):
            list_split([1, 2, 3], -1)

    def test_zero_step(self):
        """Test splitting with a zero step"""
        with self.assertRaises(ValueError):
            list_split([1, 2, 3], 0)
