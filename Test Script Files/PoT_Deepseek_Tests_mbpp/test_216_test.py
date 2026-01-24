import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset_list(['a', 'b', 'c'], ['a', 'b', 'c']))
        self.assertTrue(check_subset_list([True, False], [True, False]))

    def test_empty_lists(self):
        self.assertTrue(check_subset_list([], []))

    def test_subset_case(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2]))
        self.assertTrue(check_subset_list(['a', 'b', 'c'], ['a', 'b']))
        self.assertTrue(check_subset_list([True, False], [True]))

    def test_non_subset_case(self):
        self.assertFalse(check_subset_list([1, 2, 3], [4, 5, 6]))
        self.assertFalse(check_subset_list(['a', 'b', 'c'], ['d', 'e', 'f']))
        self.assertFalse(check_subset_list([True, False], [None]))

    def test_duplicate_elements(self):
        self.assertTrue(check_subset_list([1, 2, 2], [1, 2]))
        self.assertFalse(check_subset_list([1, 2, 2], [1, 2, 2]))
