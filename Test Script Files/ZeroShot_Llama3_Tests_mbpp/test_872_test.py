import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_subset(self):
        self.assertTrue(check_subset([1, 2, 3, 4, 5], [1, 2, 3]))
        self.assertFalse(check_subset([1, 2, 3, 4, 5], [1, 2, 3, 6]))
        self.assertTrue(check_subset([1, 2, 3, 4, 5], [1, 2]))
        self.assertFalse(check_subset([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]))
        self.assertTrue(check_subset([], []))
        self.assertFalse(check_subset([1, 2, 3, 4, 5], [6, 7, 8]))

    def test_subset_empty_list(self):
        self.assertTrue(check_subset([], []))
        self.assertFalse(check_subset([1, 2, 3, 4, 5], []))

    def test_subset_single_element(self):
        self.assertTrue(check_subset([1, 2, 3, 4, 5], [1]))
        self.assertFalse(check_subset([1, 2, 3, 4, 5], [6]))

    def test_subset_empty_list1(self):
        self.assertTrue(check_subset([], []))
        self.assertFalse(check_subset([], [1, 2, 3]))

    def test_subset_empty_list2(self):
        self.assertTrue(check_subset([], []))
        self.assertFalse(check_subset([1, 2, 3, 4, 5], []))
