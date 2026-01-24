import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_non_empty_list(self):
        self.assertFalse(empty_dit([1, 2, 3]))

    def test_list_with_mixed_elements(self):
        self.assertFalse(empty_dit([1, 2, 3, 0]))

    def test_list_with_all_zeroes(self):
        self.assertTrue(empty_dit([0, 0, 0]))

    def test_list_with_all_nonzeroes(self):
        self.assertFalse(empty_dit([1, 2, 3]))

    def test_list_with_mixed_zero_and_nonzero_elements(self):
        self.assertFalse(empty_dit([0, 1, 2, 3]))

    def test_list_with_empty_sublist(self):
        self.assertFalse(empty_dit([0, [], 1, 2]))

    def test_list_with_empty_sublist_and_nonzero_elements(self):
        self.assertFalse(empty_dit([0, [], 1, 2, 3]))

    def test_list_with_empty_sublist_and_zero_elements(self):
        self.assertTrue(empty_dit([0, [], 0]))

    def test_list_with_empty_sublist_and_mixed_elements(self):
        self.assertFalse(empty_dit([0, [], 1, 2, 3]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            empty_dit('string')
