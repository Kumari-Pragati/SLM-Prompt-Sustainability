import unittest
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], index_on_inner_list([], 0))

    def test_single_element_list(self):
        self.assertListEqual([1], index_on_inner_list([[1]], 0))
        self.assertListEqual([[1]], index_on_inner_list([[1]], 1))

    def test_multiple_elements_list(self):
        self.assertListEqual([[1, 2], [3, 4]], index_on_inner_list([[1, 2], [3, 4]], 0))
        self.assertListEqual([[1, 2], [3, 4]], index_on_inner_list([[1, 2], [3, 4]], 1))
        self.assertListEqual([[1, 2], [3, 4]], index_on_inner_list([[1, 2], [3, 4]], -1))

    def test_negative_index(self):
        self.assertRaises(IndexError, lambda: index_on_inner_list([[1, 2], [3, 4]], -2))

    def test_out_of_range_index(self):
        self.assertRaises(IndexError, lambda: index_on_inner_list([[1, 2], [3, 4]], 2))

    def test_mixed_types(self):
        self.assertRaises(TypeError, lambda: index_on_inner_list([1, 'a', [1, 2]], 0))
