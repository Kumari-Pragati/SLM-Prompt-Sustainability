import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):
    def test_subset(self):
        self.assertTrue(check_subset([1, 2, 3, 4, 5], [1, 2, 3]))

    def test_not_subset(self):
        self.assertFalse(check_subset([1, 2, 3, 4, 5], [1, 2, 3, 6]))

    def test_empty_list1(self):
        self.assertTrue(check_subset([], [1, 2, 3]))

    def test_empty_list2(self):
        self.assertTrue(check_subset([1, 2, 3], []))

    def test_single_element_list1(self):
        self.assertTrue(check_subset([1], [1]))

    def test_single_element_list2(self):
        self.assertFalse(check_subset([1], [2]))

    def test_list1_subset_of_list2(self):
        self.assertTrue(check_subset([1, 2, 3, 4, 5], [1, 2, 3, 4]))

    def test_list1_not_subset_of_list2(self):
        self.assertFalse(check_subset([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]))
