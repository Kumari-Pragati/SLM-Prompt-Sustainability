import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_non_empty_list(self):
        self.assertFalse(empty_dit([1, 2, 3]))

    def test_list_with_mixed_elements(self):
        self.assertFalse(empty_dit([1, 2, 3, 0, 4, 5]))

    def test_list_with_all_falses(self):
        self.assertTrue(empty_dit([False, False, False]))

    def test_list_with_all_trues(self):
        self.assertFalse(empty_dit([True, True, True]))

    def test_list_with_mixed_booleans(self):
        self.assertFalse(empty_dit([True, False, True]))
