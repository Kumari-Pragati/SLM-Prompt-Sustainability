import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_undulating('1212'))
        self.assertTrue(is_undulating('123123'))
        self.assertTrue(is_undulating('12321'))
        self.assertTrue(is_undulating('123321'))

    def test_single_digit(self):
        self.assertFalse(is_undulating('1'))
        self.assertFalse(is_undulating(''))

    def test_two_digits(self):
        self.assertFalse(is_undulating('12'))

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            is_undulating('12a12')
