import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):
    def test_subset_list(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2]))
    def test_not_subset_list(self):
        self.assertFalse(check_subset_list([1, 2, 3], [4, 5]))
    def test_empty_list(self):
        self.assertTrue(check_subset_list([], []))
    def test_empty_list2(self):
        self.assertFalse(check_subset_list([1, 2, 3], []))
    def test_single_element_list(self):
        self.assertTrue(check_subset_list([1], [1]))
    def test_single_element_list2(self):
        self.assertFalse(check_subset_list([1, 2, 3], [4]))
    def test_subset_list_with_duplicates(self):
        self.assertTrue(check_subset_list([1, 2, 2, 3], [1, 2, 2]))
    def test_not_subset_list_with_duplicates(self):
        self.assertFalse(check_subset_list([1, 2, 2, 3], [4, 5, 6]))
