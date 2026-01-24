import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(is_upper('abc'))
        self.assertTrue(is_upper('ABC'))
        self.assertFalse(is_upper('Abc'))

    def test_edge_conditions(self):
        self.assertTrue(is_upper(''))
        self.assertTrue(is_upper(' '))
        self.assertFalse(is_upper('a '))
        self.assertFalse(is_upper(' a'))

    def test_complex_cases(self):
        self.assertTrue(is_upper('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        self.assertFalse(is_upper('abcdefghijklmnopqrstuvwxyz'))
        self.assertFalse(is_upper('1234567890'))
        self.assertFalse(is_upper('!@#$%^&*()'))
