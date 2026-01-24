import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):

    def test_single_lowercase_char(self):
        self.assertEqual(check_char('a'), "Valid")

    def test_multiple_lowercase_chars(self):
        self.assertEqual(check_char('abc'), "Invalid")

    def test_single_uppercase_char(self):
        self.assertEqual(check_char('A'), "Invalid")

    def test_numeric_char(self):
        self.assertEqual(check_char('1'), "Invalid")

    def test_special_char(self):
        self.assertEqual(check_char('@'), "Invalid")

    def test_empty_string(self):
        self.assertEqual(check_char(''), "Invalid")

    def test_whitespace(self):
        self.assertEqual(check_char(' '), "Invalid")

    def test_string_with_whitespace(self):
        self.assertEqual(check_char('a b'), "Invalid")

    def test_string_with_special_characters(self):
        self.assertEqual(check_char('a@b'), "Invalid")

    def test_string_with_numeric_characters(self):
        self.assertEqual(check_char('a1b'), "Invalid")

    def test_string_with_uppercase_characters(self):
        self.assertEqual(check_char('Ab'), "Invalid")
