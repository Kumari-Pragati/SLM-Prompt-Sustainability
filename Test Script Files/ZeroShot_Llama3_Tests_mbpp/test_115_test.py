import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_non_empty_list(self):
        self.assertFalse(empty_dit([1, 2, 3]))

    def test_list_with_mixed_elements(self):
        self.assertFalse(empty_dit([1, 2, 0, 3]))

    def test_list_with_all_zeroes(self):
        self.assertTrue(empty_dit([0, 0, 0]))

    def test_list_with_all_non_zeroes(self):
        self.assertFalse(empty_dit([1, 2, 3]))

    def test_list_with_mixed_zero_and_non_zero_elements(self):
        self.assertFalse(empty_dit([1, 0, 2]))
