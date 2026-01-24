import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):
    def test_valid_single_char(self):
        self.assertEqual(check_char("a"), "Valid")

    def test_valid_multiple_chars(self):
        self.assertEqual(check_char("abc"), "Valid")

    def test_valid_char_with_spaces(self):
        self.assertEqual(check_char("a b c"), "Valid")

    def test_invalid_single_char(self):
        self.assertEqual(check_char("A"), "Invalid")

    def test_invalid_multiple_chars(self):
        self.assertEqual(check_char("abc123"), "Invalid")

    def test_invalid_char_with_spaces(self):
        self.assertEqual(check_char("a b 123"), "Invalid")

    def test_empty_string(self):
        self.assertEqual(check_char(""), "Invalid")
