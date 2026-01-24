import unittest
from mbpp_69_code import is_sublist

class TestIsSublist(unittest.TestCase):

    def test_empty_sublist(self):
        self.assertTrue(is_sublist([], []))

    def test_empty_mainlist(self):
        self.assertTrue(is_sublist([], [1, 2, 3]))

    def test_sublist(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [2, 3, 4]))

    def test_sublist_with_overlap(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5, 2, 3, 4], [2, 3, 4]))

    def test_sublist_with_overlap_at_end(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5, 2, 3, 4, 5], [2, 3, 4]))

    def test_sublist_with_overlap_at_start(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5, 2, 3, 4], [2, 3, 4]))

    def test_sublist_with_overlap_at_start_and_end(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5, 2, 3, 4, 5], [2, 3, 4]))

    def test_mainlist_longer_than_sublist(self):
        self.assertFalse(is_sublist([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4]))

    def test_sublist_longer_than_mainlist(self):
        self.assertFalse(is_sublist([1, 2], [1, 2, 3, 4, 5]))

    def test_sublist_not_found(self):
        self.assertFalse(is_sublist([1, 2, 3, 4, 5], [6, 7, 8]))

    def test_sublist_with_duplicates(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 4, 5], [2, 2, 3, 4]))

    def test_sublist_with_duplicates_at_start(self):
        self.assertTrue(is_sublist([1, 1, 2, 3, 4, 5], [1, 1, 2]))

    def test_sublist_with_duplicates_at_end(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5, 5, 5], [5, 5, 5]))

    def test_sublist_with_duplicates_at_start_and_end(self):
        self.assertTrue(is_sublist([1, 1, 2, 3, 4, 5, 5, 5], [1, 1, 2, 5, 5]))
