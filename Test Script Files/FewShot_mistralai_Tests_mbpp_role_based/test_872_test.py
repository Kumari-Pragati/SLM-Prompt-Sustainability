import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):
    def test_subsets(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2]))
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3, 4]))

    def test_empty_lists(self):
        self.assertFalse(check_subset([], []))
        self.assertFalse(check_subset([1, 2, 3], []))
        self.assertFalse(check_subset([], [1, 2, 3]))

    def test_single_element_lists(self):
        self.assertTrue(check_subset([1], [1]))
        self.assertFalse(check_subset([1], [2]))
        self.assertFalse(check_subset([2], [1]))

    def test_one_in_other(self):
        self.assertTrue(check_subset([1, 2], [2, 1]))
        self.assertFalse(check_subset([1, 2], [3]))
        self.assertFalse(check_subset([3], [1, 2]))

    def test_duplicates(self):
        self.assertTrue(check_subset([1, 1, 2], [1, 1, 2]))
        self.assertTrue(check_subset([1, 2, 2], [1, 2, 2]))
        self.assertTrue(check_subset([2, 2, 3], [2, 2, 3]))
