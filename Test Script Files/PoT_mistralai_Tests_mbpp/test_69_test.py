import unittest
from mbpp_69_code import is_sublist

class TestIsSublist(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(is_sublist([], []))
        self.assertFalse(is_sublist([1, 2, 3], []))

    def test_equal_lists(self):
        self.assertTrue(is_sublist([1, 2, 3], [1, 2, 3]))
        self.assertTrue(is_sublist([], []))

    def test_longer_list(self):
        self.assertFalse(is_sublist([1, 2, 3], [1, 2, 3, 4]))
        self.assertFalse(is_sublist([], [1, 2, 3]))

    def test_shorter_list(self):
        self.assertTrue(is_sublist([1, 2, 3], [1, 2]))
        self.assertFalse(is_sublist([1, 2], [1, 2, 3]))

    def test_mixed_types(self):
        self.assertFalse(is_sublist([1, 2, 3], [1, '2', 3]))
        self.assertFalse(is_sublist([1, 2, 3], [1, 2, '3']))

    def test_duplicates(self):
        self.assertTrue(is_sublist([1, 2, 1, 2], [1, 2]))
        self.assertTrue(is_sublist([1, 2, 1, 2], [2, 1, 2]))
