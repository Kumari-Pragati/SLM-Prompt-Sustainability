import unittest
from mbpp_857_code import listify_list

class TestListifyList(unittest.TestCase):

    def test_listify_list_normal(self):
        self.assertListEqual(listify_list([[1, 2, 3], [4, 5, 6]]), [[[1, 2, 3]], [[4, 5, 6]]])

    def test_listify_list_empty_list(self):
        self.assertListEqual(listify_list([]), [])

    def test_listify_list_single_element(self):
        self.assertListEqual(listify_list([1]), [[1]])

    def test_listify_list_single_empty_list(self):
        self.assertListEqual(listify_list([[]]], [[[]]])

    def test_listify_list_list_of_strings(self):
        self.assertListEqual(listify_list(['a', 'b', 'c']), [['a'], ['b'], ['c']])

    def test_listify_list_list_of_lists_of_lists(self):
        self.assertListEqual(listify_list([[[1], [2]], [[3], [4]]]), [[[[1]], [[2]]], [[[3]], [[4]]]])

    def test_listify_list_list_of_tuples(self):
        self.assertListEqual(listify_list([(1, 2, 3), (4, 5, 6)]), [[(1, 2, 3)], [(4, 5, 6)]])
