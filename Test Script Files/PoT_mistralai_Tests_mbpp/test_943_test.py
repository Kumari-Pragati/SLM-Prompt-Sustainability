import unittest
from mbpp_943_code import combine_lists

class TestCombineLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(combine_lists([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_edge_case_empty_lists(self):
        self.assertListEqual(combine_lists([], []), [])

    def test_edge_case_one_list_empty(self):
        self.assertListEqual(combine_lists([], [1, 2, 3]), [1, 2, 3])
        self.assertListEqual(combine_lists([1, 2, 3], []), [1, 2, 3])

    def test_edge_case_single_element_lists(self):
        self.assertListEqual(combine_lists([1], [2]), [1, 2])
        self.assertListEqual(combine_lists([2], [1]), [1, 2])

    def test_corner_case_duplicates(self):
        self.assertListEqual(combine_lists([1, 1, 2], [2, 2]), [1, 1, 2, 2])
