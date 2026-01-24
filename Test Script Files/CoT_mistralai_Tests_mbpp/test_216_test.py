import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):
    def test_empty_lists(self):
        self.assertTrue(check_subset_list([], []))
        self.assertFalse(check_subset_list([1], []))
        self.assertFalse(check_subset_list([], [1]))

    def test_single_elements(self):
        self.assertTrue(check_subset_list([1], [1]))
        self.assertFalse(check_subset_list([2], [1]))

    def test_equal_lists(self):
        self.assertTrue(check_subset_list([1, 2], [1, 2]))
        self.assertTrue(check_subset_list([2, 1], [1, 2]))

    def test_subsets(self):
        self.assertTrue(check_subset_list([1, 2], [1, 2, 3]))
        self.assertTrue(check_subset_list([2, 1], [1, 2, 3]))
        self.assertTrue(check_subset_list([3, 2, 1], [1, 2, 3]))

    def test_non_subsets(self):
        self.assertFalse(check_subset_list([1, 2], [3, 4]))
        self.assertFalse(check_subset_list([3, 4], [1, 2]))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, check_subset_list, 1, [1, 2])
        self.assertRaises(TypeError, check_subset_list, [1], "list2")
