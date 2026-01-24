import unittest
from92_code import is_undulating

class TestIsUndulating(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(is_undulating([]))

    def test_single_element(self):
        self.assertFalse(is_undulating([1]))

    def test_two_elements(self):
        self.assertFalse(is_undulating([1, 1]))

    def test_three_elements(self):
        self.assertTrue(is_undulating([1, 2, 1]))
        self.assertFalse(is_undulating([1, 2, 2]))

    def test_four_elements(self):
        self.assertTrue(is_undulating([1, 2, 3, 2]))
        self.assertFalse(is_undulating([1, 2, 3, 1]))

    def test_longer_list(self):
        self.assertTrue(is_undulating([1, 2, 3, 4, 5, 4, 3, 2, 1]))

    def test_negative_numbers(self):
        self.assertTrue(is_undulating([-1, -2, -1]))
        self.assertFalse(is_undulating([-1, -2, -3]))

    def test_mixed_numbers(self):
        self.assertTrue(is_undulating([1, -2, 1]))
        self.assertFalse(is_undulating([1, -2, -3]))
