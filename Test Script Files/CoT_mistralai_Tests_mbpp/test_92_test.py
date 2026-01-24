import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(is_undulating([]))

    def test_single_element_list(self):
        self.assertFalse(is_undulating([1]))

    def test_two_element_list(self):
        self.assertFalse(is_undulating([1, 1]))

    def test_three_element_list(self):
        self.assertFalse(is_undulating([1, 2, 1]))

    def test_undulating_list(self):
        self.assertTrue(is_undulating([1, 2, 3, 2, 1]))

    def test_non_undulating_list(self):
        self.assertFalse(is_undulating([1, 1, 2, 1]))

    def test_list_with_duplicates(self):
        self.assertTrue(is_undulating([1, 1, 2, 1, 1]))

    def test_list_with_negative_numbers(self):
        self.assertTrue(is_undulating([1, -2, 3, -2, 1]))

    def test_list_with_floats(self):
        self.assertTrue(is_undulating([1.0, 2.0, 3.0, 2.0, 1.0]))
