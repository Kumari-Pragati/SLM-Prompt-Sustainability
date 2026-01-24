import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):
    def test_undulating_sequence(self):
        self.assertTrue(is_undulating([1, 2, 1]))
        self.assertTrue(is_undulating([3, 2, 1, 3]))

    def test_non_undulating_sequence(self):
        self.assertFalse(is_undulating([1, 1, 1]))
        self.assertFalse(is_undulating([2, 2, 2]))

    def test_empty_sequence(self):
        self.assertFalse(is_undulating([]))

    def test_single_element_sequence(self):
        self.assertFalse(is_undulating([1]))

    def test_two_element_sequence(self):
        self.assertFalse(is_undulating([1, 1]))
