import unittest
from mbpp_69_code import is_sublist

class TestIsSublist(unittest.TestCase):
    def test_empty_sublist(self):
        self.assertTrue(is_sublist([], []))

    def test_equal_lists(self):
        self.assertTrue(is_sublist([1, 2, 3], [1, 2, 3]))

    def test_sublist_at_start(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [1, 2]))

    def test_sublist_in_middle(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [3, 4]))

    def test_sublist_at_end(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [4, 5]))

    def test_non_sublist(self):
        self.assertFalse(is_sublist([1, 2, 3, 4, 5], [6, 7]))

    def test_same_elements_different_order(self):
        self.assertFalse(is_sublist([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))

    def test_empty_superlist(self):
        self.assertFalse(is_sublist([], [1, 2, 3]))

    def test_empty_sublist_in_superlist(self):
        self.assertTrue(is_sublist([1, 2, 3, 0, 4, 5], []))

    def test_superlist_with_duplicates(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5], [2, 2]))

    def test_sublist_with_duplicates(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5], [2, 2]))

    def test_superlist_with_duplicates_and_sublist_with_duplicates(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5], [2, 2]))

    def test_large_lists(self):
        superlist = list(range(1, 10001))
        sublist = list(range(5001, 10001))
        self.assertTrue(is_sublist(superlist, sublist))
