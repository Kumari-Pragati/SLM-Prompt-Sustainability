import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2]))

    def test_empty_list1(self):
        self.assertFalse(check_subset([], [1, 2]))

    def test_empty_list2(self):
        self.assertTrue(check_subset([1, 2], []))

    def test_single_element_list1(self):
        self.assertTrue(check_subset([1], [1]))

    def test_single_element_list2(self):
        self.assertFalse(check_subset([1], [2]))

    def test_subset_of_subset(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2]))

    def test_non_subset(self):
        self.assertFalse(check_subset([1, 2, 3], [4, 5]))

    def test_list1_longer_than_list2(self):
        self.assertTrue(check_subset([1, 2, 3, 4, 5], [1, 2]))

    def test_list2_longer_than_list1(self):
        self.assertFalse(check_subset([1, 2], [1, 2, 3]))
