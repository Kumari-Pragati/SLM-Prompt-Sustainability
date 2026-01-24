import unittest
from mbpp_857_code import listify_list

class TestListifyList(unittest.TestCase):

    def test_simple_list(self):
        self.assertListEqual(listify_list([[1, 2, 3], [4, 5, 6]]), [[[1, 2, 3]], [[4, 5, 6]]])

    def test_empty_list(self):
        self.assertListEqual(listify_list([]), [[]])

    def test_single_element_list(self):
        self.assertListEqual(listify_list([[1]]), [[[1]]])

    def test_list_of_scalars(self):
        self.assertListEqual(listify_list([1, 2, 3]), [[1], [2], [3]])

    def test_list_of_lists_with_scalars(self):
        self.assertListEqual(listify_list([[1], [2, 3], [4]]), [[[1]], [[2, 3]], [[4]]])

    def test_list_of_lists_with_lists(self):
        self.assertListEqual(listify_list([[[1], [2]], [[3], [4]]]), [[[[1], [2]]], [[[3], [4]]]])
