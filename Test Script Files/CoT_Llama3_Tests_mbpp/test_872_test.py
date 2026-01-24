import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):
    def test_subset_true(self):
        self.assertTrue(check_subset([1, 2, 3, 4, 5], [1, 2, 3]))

    def test_subset_false(self):
        self.assertFalse(check_subset([1, 2, 3, 4, 5], [6, 7, 8]))

    def test_subset_empty(self):
        self.assertTrue(check_subset([], []))

    def test_subset_single_element(self):
        self.assertTrue(check_subset([1], [1]))

    def test_subset_empty_list2(self):
        self.assertTrue(check_subset([1, 2, 3], []))

    def test_subset_list1_empty(self):
        self.assertFalse(check_subset([], [1, 2, 3]))

    def test_subset_list1_single_element(self):
        self.assertFalse(check_subset([1], [2]))

    def test_subset_list1_empty_list2_empty(self):
        self.assertTrue(check_subset([], []))

    def test_subset_list1_empty_list2_non_empty(self):
        self.assertFalse(check_subset([], [1, 2, 3]))

    def test_subset_list1_non_empty_list2_empty(self):
        self.assertFalse(check_subset([1, 2, 3], []))
