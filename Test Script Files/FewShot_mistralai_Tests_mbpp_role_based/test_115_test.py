import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_single_element_list(self):
        self.assertFalse(empty_dit([1]))

    def test_multiple_elements_list(self):
        self.assertFalse(empty_dit([1, 2, 3]))

    def test_list_with_empty_string(self):
        self.assertFalse(empty_dit(["", 1, 2, 3]))

    def test_list_with_none(self):
        self.assertFalse(empty_dit([None, 1, 2, 3]))
