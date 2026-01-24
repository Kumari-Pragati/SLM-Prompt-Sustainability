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

    def test_superlist_shorter_than_sublist(self):
        self.assertFalse(is_sublist([1, 2], [1, 2, 3]))

    def test_superlist_longer_than_sublist(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5, 6], [1, 2, 3]))

    def test_single_element_sublist(self):
        self.assertTrue(is_sublist([1, 2, 3, 4, 5], [1]))

    def test_single_element_superlist(self):
        self.assertFalse(is_sublist([1], [1, 2, 3]))

    def test_sublist_with_duplicates(self):
        self.assertTrue(is_sublist([1, 2, 2, 3, 4, 5], [2, 2]))

    def test_invalid_input_sublist(self):
        with self.assertRaises(TypeError):
            is_sublist([1, 2, 3], 'invalid')

    def test_invalid_input_superlist(self):
        with self.assertRaises(TypeError):
            is_sublist('invalid', [1, 2, 3])
