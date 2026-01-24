import unittest
from mbpp_69_code import is_sublist

class TestIsSublist(unittest.TestCase):
    def test_empty_sublist(self):
        self.assertTrue(is_sublist([], []))

    def test_sublist_is_empty(self):
        self.assertTrue(is_sublist([1, 2, 3], []))

    def test_sublist_is_equal_to_list(self):
        self.assertTrue(is_sublist([1, 2, 3], [1, 2, 3]))

    def test_sublist_is_not_in_list(self):
        self.assertFalse(is_sublist([1, 2, 3], [4, 5, 6]))

    def test_sublist_is_in_list(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [2, 3, 4]))

    def test_sublist_is_at_beginning(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [1, 2]))

    def test_sublist_is_at_end(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [4, 5]))

    def test_sublist_is_in_middle(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5, 6], [3, 4]))

    def test_sublist_is_not_in_list_with_duplicates(self):
        self.assertFalse(is_sublist([1, 2, 2, 3, 3, 4], [2, 2, 3]))
