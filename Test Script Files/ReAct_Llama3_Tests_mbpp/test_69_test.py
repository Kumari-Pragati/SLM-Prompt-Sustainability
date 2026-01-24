import unittest
from mbpp_69_code import is_sublist

class TestIsSublist(unittest.TestCase):

    def test_empty_sublist(self):
        self.assertTrue(is_sublist([], []))

    def test_empty_mainlist(self):
        self.assertFalse(is_sublist([1, 2, 3], [4, 5, 6]))

    def test_sublist(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [2, 3, 4]))

    def test_sublist_at_start(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [1, 2]))

    def test_sublist_at_end(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [4, 5]))

    def test_sublist_at_middle(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [2, 3, 4]))

    def test_sublist_with_duplicates(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 4, 5], [2, 2, 4]))

    def test_sublist_with_duplicates_at_start(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 4, 5], [1, 2, 2]))

    def test_sublist_with_duplicates_at_end(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 4, 5], [4, 4, 5]))

    def test_sublist_with_duplicates_at_middle(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 4, 5], [2, 2, 4]))

    def test_sublist_with_duplicates_at_start_and_end(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 4, 5], [1, 2, 2, 4, 4, 5]))

    def test_sublist_with_duplicates_at_start_and_middle(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 4, 5], [1, 2, 2, 4]))

    def test_sublist_with_duplicates_at_end_and_middle(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 4, 5], [2, 2, 4, 4]))

    def test_sublist_with_duplicates_at_start_and_middle_and_end(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 4, 5], [1, 2, 2, 4, 4]))

    def test_sublist_with_duplicates_at_start_and_end(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 4, 5], [1, 2, 2, 4, 4, 5]))

    def test_sublist_with_duplicates_at_start_and_middle_and_end(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 4, 5], [1, 2, 2, 4, 4]))

    def test_sublist_with_duplicates_at_start_and_end_and_middle(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 4, 5], [1, 2, 2, 4, 4, 5]))

    def test_sublist_with_duplicates_at_start_and_end_and_middle_and_end(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 4, 5], [1, 2, 2, 4, 4, 5]))

    def test_sublist_with_duplicates_at_start_and_end_and_middle_and_end(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 4, 5], [1, 2, 2, 4, 4, 5]))

    def test_sublist_with_duplicates_at_start_and_end_and_middle_and_end(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 4, 5], [1, 2, 2, 4, 4, 5])

    def test_sublist_with_duplicates_at_start_and_end_and_middle_and_end(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4,