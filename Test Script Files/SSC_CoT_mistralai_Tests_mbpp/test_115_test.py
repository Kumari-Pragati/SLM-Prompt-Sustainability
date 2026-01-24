import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):
    def test_normal_input(self):
        self.assertTrue(empty_dit([]))

    def test_list_with_empty_elements(self):
        self.assertTrue(empty_dit([None, [], (), {}, set(), frozenset(), 0.0]))

    def test_single_element(self):
        self.assertFalse(empty_dit([1]))
        self.assertFalse(empty_dit([None]])
        self.assertFalse(empty_dit([0.0]])
        self.assertFalse(empty_dit([False]])

    def test_multiple_elements(self):
        self.assertFalse(empty_dit([1, 2, 3]))
        self.assertFalse(empty_dit([None, None]))
        self.assertFalse(empty_dit([0.0, 0.0]))
        self.assertFalse(empty_dit([False, False]))

    def test_mixed_types(self):
        self.assertFalse(empty_dit([1, "str", 2.0]))
        self.assertFalse(empty_dit([None, 1, 2.0]))
        self.assertFalse(empty_dit([0.0, "str", False]))
