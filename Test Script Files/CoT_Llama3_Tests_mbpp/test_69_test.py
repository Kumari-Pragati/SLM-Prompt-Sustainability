import unittest
from mbpp_69_code import is_sublist

class TestIsSublist(unittest.TestCase):
    def test_empty_sublist(self):
        self.assertTrue(is_sublist([], []))

    def test_empty_mainlist(self):
        self.assertFalse(is_sublist([1, 2, 3], [4, 5, 6]))

    def test_sublist(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [2, 3, 4]))

    def test_sublist_with_duplicates(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5], [2, 2, 3, 4]))

    def test_sublist_with_duplicates_in_mainlist(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5, 2], [2, 2, 3, 4]))

    def test_sublist_with_duplicates_in_sublist(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5, 2, 2], [2, 2, 3, 4]))

    def test_sublist_with_duplicates_in_mainlist_and_sublist(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5, 2, 2, 2], [2, 2, 3, 4]))

    def test_sublist_with_duplicates_in_mainlist_and_sublist_with_duplicates(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5, 2, 2, 2, 2], [2, 2, 3, 4]))

    def test_sublist_with_duplicates_in_mainlist_and_sublist_with_duplicates_and_duplicates_in_sublist(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5, 2, 2, 2, 2, 2], [2, 2, 3, 4]))

    def test_sublist_with_duplicates_in_mainlist_and_sublist_with_duplicates_and_duplicates_in_sublist_and_duplicates_in_mainlist(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5, 2, 2, 2, 2, 2, 2], [2, 2, 3, 4]))

    def test_sublist_with_duplicates_in_mainlist_and_sublist_with_duplicates_and_duplicates_in_sublist_and_duplicates_in_mainlist_and_duplicates_in_sublist(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2], [2, 2, 3, 4]))

    def test_sublist_with_duplicates_in_mainlist_and_sublist_with_duplicates_and_duplicates_in_sublist_and_duplicates_in_mainlist_and_duplicates_in_sublist_and_duplicates_in_mainlist(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 3, 4]))

    def test_sublist_with_duplicates_in_mainlist_and_sublist_with_duplicates_and_duplicates_in_sublist_and_duplicates_in_mainlist_and_duplicates_in_sublist_and_duplicates_in_mainlist_and_duplicates_in_sublist(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 3, 4]))

    def test_sublist_with_duplicates_in_mainlist_and_sublist_with_duplicates_and_duplicates_in_sublist_and_duplicates_in_mainlist_and_duplicates_in_sublist_and_duplicates_in_mainlist_and_duplicates_in_sublist_and_duplicates_in_mainlist(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 3, 4]))

    def test_sublist_with_duplicates_in_mainlist_and_sublist_with_duplicates_and_duplicates_in_sublist_and_duplicates_in_mainlist_and_duplicates_in_sublist_and_duplicates_in_mainlist_and_duplicates_in_sublist_and_duplicates_in_mainlist_and_duplicates_in_sublist(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5, 2, 2,