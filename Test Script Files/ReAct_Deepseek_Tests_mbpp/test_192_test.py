import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_String('a1'))

    def test_only_letters(self):
        self.assertFalse(check_String('abc'))

    def test_only_numbers(self):
        self.assertFalse(check_String('123'))

    def test_empty_string(self):
        self.assertFalse(check_String(''))

    def test_special_characters(self):
        self.assertFalse(check_String('a@1'))

    def test_mixed_case(self):
        self.assertTrue(check_String('aB1'))

    def test_mixed_case_with_special_characters(self):
        self.assertFalse(check_String('aB1@'))
