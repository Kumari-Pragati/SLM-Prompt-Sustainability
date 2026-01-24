import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_String('abc123'))

    def test_no_letters(self):
        self.assertFalse(check_String('123456'))

    def test_no_numbers(self):
        self.assertFalse(check_String('abcdef'))

    def test_empty_string(self):
        self.assertFalse(check_String(''))

    def test_special_characters(self):
        self.assertFalse(check_String('abcde!@#'))

    def test_mixed_case(self):
        self.assertTrue(check_String('abc123XYZ'))

    def test_mixed_case_and_special_characters(self):
        self.assertFalse(check_String('abc123XYZ!@#'))
