import unittest
from mbpp_857_code import listify_list

class TestListifyList(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(listify_list([[1, 2, 3], [4, 5, 6]]), [[[1, 2, 3]], [[4, 5, 6]]])

    def test_empty_list(self):
        self.assertListEqual(listify_list([]), [])

    def test_single_element_list(self):
        self.assertListEqual(listify_list([[1]]), [[[1]]])

    def test_list_with_string(self):
        self.assertListEqual(listify_list([['a', 'b', 'c']]), [[['a'], ['b'], ['c']]])

    def test_list_with_mixed_types(self):
        self.assertListEqual(listify_list([[1, 'a'], [2, 'b']]), [[[1, 'a']], [[2, 'b']]])

    def test_list_with_nested_lists(self):
        self.assertListEqual(listify_list([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]), [[[[1, 2]], [ [3, 4] ]], [[[5, 6]], [ [7, 8] ]]])
