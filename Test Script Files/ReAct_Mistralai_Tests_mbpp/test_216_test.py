import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):

    def test_empty_lists(self):
        self.assertTrue(check_subset_list([], []))
        self.assertFalse(check_subset_list([1], []))
        self.assertFalse(check_subset_list([], [1]))

    def test_single_element_lists(self):
        self.assertTrue(check_subset_list([1], [1]))
        self.assertFalse(check_subset_list([1], [2]))

    def test_equal_lists(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset_list([3, 2, 1], [1, 2, 3]))

    def test_subset_lists(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2, 3, 4]))
        self.assertTrue(check_subset_list([3, 2, 1], [1, 2, 3, 4, 5]))

    def test_non_subset_lists(self):
        self.assertFalse(check_subset_list([1, 2, 3], [4, 5, 6]))
        self.assertFalse(check_subset_list([3, 2, 1], [1, 2, 5, 6]))

    def test_lists_with_duplicates(self):
        self.assertTrue(check_subset_list([1, 1, 2, 3], [1, 2, 3]))
        self.assertFalse(check_subset_list([1, 1, 2, 3], [4, 5, 6]))

    def test_lists_with_non_numeric_elements(self):
        self.assertRaises(TypeError, check_subset_list, ['a', 'b', 'c'], [1, 2, 3])
        self.assertRaises(TypeError, check_subset_list, [1, 2, 3], ['a', 'b', 'c'])
