import unittest
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], index_on_inner_list([], 0))

    def test_single_element_list(self):
        self.assertListEqual([1], index_on_inner_list([[1]], 0))
        self.assertListEqual([[1]], index_on_inner_list([[1]], 1))

    def test_simple_list(self):
        self.assertListEqual([[1, 2], [3, 4], [5, 6]], index_on_inner_list([[1, 2], [3, 4], [5, 6]], 0))
        self.assertListEqual([[1, 2], [3, 4], [5, 6]], index_on_inner_list([[1, 2], [3, 4], [5, 6]], 1))

    def test_negative_index(self):
        self.assertRaises(IndexError, lambda: index_on_inner_list([[1, 2], [3, 4], [5, 6]], -1))

    def test_invalid_input(self):
        self.assertRaises(TypeError, lambda: index_on_inner_list('invalid', 0))
        self.assertRaises(TypeError, lambda: index_on_inner_list([1], 'invalid'))
