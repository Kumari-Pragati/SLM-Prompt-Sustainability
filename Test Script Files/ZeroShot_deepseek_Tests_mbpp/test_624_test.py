import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):

    def test_all_upper(self):
        self.assertTrue(is_upper('ABC'))

    def test_mixed_case(self):
        self.assertFalse(is_upper('AbC'))

    def test_all_lower(self):
        self.assertFalse(is_upper('abc'))

    def test_numbers_and_symbols(self):
        self.assertFalse(is_upper('123@#'))

    def test_empty_string(self):
        self.assertTrue(is_upper(''))
