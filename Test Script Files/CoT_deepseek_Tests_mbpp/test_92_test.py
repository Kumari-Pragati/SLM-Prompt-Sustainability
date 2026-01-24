import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):

    def test_single_digit(self):
        self.assertFalse(is_undulating(1))

    def test_double_digit(self):
        self.assertFalse(is_undulating(12))

    def test_undulating_sequence(self):
        self.assertTrue(is_undulating('99'))
        self.assertTrue(is_undulating('7777'))
        self.assertTrue(is_undulating('11111111'))

    def test_non_undulating_sequence(self):
        self.assertFalse(is_undulating('123'))
        self.assertFalse(is_undulating('12121212'))

    def test_empty_string(self):
        self.assertFalse(is_undulating(''))

    def test_single_character_repetition(self):
        self.assertTrue(is_undulating('7'))

    def test_large_undulating_sequence(self):
        self.assertTrue(is_undulating('9'*10000))

    def test_large_non_undulating_sequence(self):
        self.assertFalse(is_undulating('1'*10001))
