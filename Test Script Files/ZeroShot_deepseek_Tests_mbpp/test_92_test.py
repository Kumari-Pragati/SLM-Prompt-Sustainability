import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):

    def test_single_digit(self):
        self.assertFalse(is_undulating('1'))

    def test_double_digit(self):
        self.assertFalse(is_undulating('11'))

    def test_short_undulating(self):
        self.assertFalse(is_undulating('111'))

    def test_long_undulating(self):
        self.assertTrue(is_undulating('1111111111'))

    def test_mixed_undulating(self):
        self.assertFalse(is_undulating('1212121212'))

    def test_empty_string(self):
        self.assertFalse(is_undulating(''))

    def test_large_undulating(self):
        self.assertTrue(is_undulating('1' * 10000))
