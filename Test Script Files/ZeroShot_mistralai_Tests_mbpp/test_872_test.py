import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_empty_lists(self):
        self.assertTrue(check_subset([], []))

    def test_one_element_lists(self):
        self.assertTrue(check_subset([1], [1]))
        self.assertFalse(check_subset([1], []))
        self.assertFalse(check_subset([], [1]))

    def test_equal_lists(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3]))

    def test_subset_lists(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3, 4]))
        self.assertTrue(check_subset([2, 3, 4], [1, 2, 3, 4]))

    def test_non_subset_lists(self):
        self.assertFalse(check_subset([1, 2, 3], [4, 5, 6]))
        self.assertFalse(check_subset([4, 5, 6], [1, 2, 3]))

    def test_lists_with_duplicates(self):
        self.assertTrue(check_subset([1, 1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset([1, 2, 2, 3], [1, 2, 3]))
