import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_list_with_all_true(self):
        self.assertFalse(empty_dit([True, True, True]))

    def test_list_with_all_false(self):
        self.assertTrue(empty_dit([False, False, False]))

    def test_list_with_mixed_values(self):
        self.assertFalse(empty_dit([True, False, True]))

    def test_list_with_non_boolean_values(self):
        with self.assertRaises(TypeError):
            empty_dit([1, 2, 3])
