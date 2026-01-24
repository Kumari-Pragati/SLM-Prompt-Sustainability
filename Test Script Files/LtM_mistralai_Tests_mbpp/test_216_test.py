import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):

    def test_simple_subset(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2]))
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset_list([1, 2], [1, 2, 3]))

    def test_empty_lists(self):
        self.assertTrue(check_subset_list([], []))
        self.assertFalse(check_subset_list([1], []))
        self.assertFalse(check_subset_list([], [1]))

    def test_single_element_lists(self):
        self.assertTrue(check_subset_list([1], [1]))
        self.assertFalse(check_subset_list([2], [1]))

    def test_edge_cases(self):
        self.assertTrue(check_subset_list([1, 2, 3], [2, 1, 3]))
        self.assertFalse(check_subset_list([1, 2, 3], [4, 5, 6]))
        self.assertFalse(check_subset_list([1, 2, 3], [1, 2, 4]))

    def test_reversed_lists(self):
        self.assertTrue(check_subset_list([1, 2], [2, 1]))
        self.assertFalse(check_subset_list([1, 2, 3], [3, 2, 1]))
