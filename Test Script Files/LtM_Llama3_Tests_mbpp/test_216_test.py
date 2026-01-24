import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2, 3]))

    def test_empty_list1(self):
        self.assertFalse(check_subset_list([], [1, 2, 3]))

    def test_empty_list2(self):
        self.assertTrue(check_subset_list([1, 2, 3], []))

    def test_subset(self):
        self.assertTrue(check_subset_list([1, 2, 3, 4], [1, 2, 3]))

    def test_not_subset(self):
        self.assertFalse(check_subset_list([1, 2, 3], [4, 5, 6]))

    def test_subset_with_duplicates(self):
        self.assertTrue(check_subset_list([1, 2, 2, 3], [1, 2, 2]))

    def test_not_subset_with_duplicates(self):
        self.assertFalse(check_subset_list([1, 2, 3], [4, 5, 6]))
