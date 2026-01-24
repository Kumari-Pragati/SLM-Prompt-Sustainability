import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_empty_lists(self):
        self.assertTrue(check_subset([], []))

    def test_subset_at_start(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2]))

    def test_subset_in_middle(self):
        self.assertTrue(check_subset([1, 2, 3, 4, 5], [2, 3]))

    def test_subset_at_end(self):
        self.assertTrue(check_subset([1, 2, 3], [2, 3]))

    def test_not_subset(self):
        self.assertFalse(check_subset([1, 2, 3], [4, 5]))

    def test_equal_lists(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3]))

    def test_empty_list1(self):
        self.assertFalse(check_subset([], [1, 2, 3]))

    def test_empty_list2(self):
        self.assertTrue(check_subset([1, 2, 3], []))
