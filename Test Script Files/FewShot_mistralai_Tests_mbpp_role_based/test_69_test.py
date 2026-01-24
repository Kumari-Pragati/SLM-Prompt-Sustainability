import unittest
from mbpp_69_code import is_sublist

class TestIsSublist(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(is_sublist([], []))

    def test_equal_lists(self):
        self.assertTrue(is_sublist([1, 2, 3], [1, 2, 3]))

    def test_longer_list(self):
        self.assertFalse(is_sublist([1, 2, 3], [1, 2, 3, 4]))

    def test_shorter_list(self):
        self.assertTrue(is_sublist([1, 2, 3], [1, 2]))

    def test_mismatched_lists(self):
        self.assertFalse(is_sublist([1, 2, 3], [3, 2, 1]))

    def test_list_with_duplicates(self):
        self.assertTrue(is_sublist([1, 1, 2, 3], [1, 2]))

    def test_list_with_non_list(self):
        self.assertRaises(TypeError, is_sublist, [1, 2, 3], "not_a_list")
