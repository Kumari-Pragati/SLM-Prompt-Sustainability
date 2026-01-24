import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):

    def test_empty_lists(self):
        self.assertTrue(check_subset_list([], []))

    def test_subset_lists(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2]))

    def test_non_subset_lists(self):
        self.assertFalse(check_subset_list([1, 2, 3], [4, 5]))

    def test_equal_lists(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2, 3]))

    def test_duplicate_elements(self):
        self.assertTrue(check_subset_list([1, 2, 2], [1, 2]))
        self.assertFalse(check_subset_list([1, 2, 2], [1, 2, 3]))
