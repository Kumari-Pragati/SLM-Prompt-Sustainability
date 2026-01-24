import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_non_empty_list(self):
        self.assertFalse(empty_dit([1, 2, 3]))

    def test_list_with_mixed_elements(self):
        self.assertFalse(empty_dit([1, 2, [], 4]))

    def test_list_with_all_empty_elements(self):
        self.assertTrue(empty_dit([[], [], []]))

    def test_list_with_non_empty_and_empty_elements(self):
        self.assertFalse(empty_dit([1, [], 3]))

    def test_list_with_empty_and_non_empty_elements_mixed(self):
        self.assertFalse(empty_dit([1, [], 2, [], 3]))
