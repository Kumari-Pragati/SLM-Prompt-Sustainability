import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):

    def test_valid_lowercase(self):
        self.assertEqual(check_char("a"), "Valid")

    def test_invalid_uppercase(self):
        self.assertEqual(check_char("A"), "Invalid")

    def test_valid_lowercase_with_spaces(self):
        self.assertEqual(check_char("a b"), "Valid")

    def test_invalid_uppercase_with_spaces(self):
        self.assertEqual(check_char("A b"), "Invalid")

    def test_valid_lowercase_with_repeated_chars(self):
        self.assertEqual(check_char("aa"), "Valid")

    def test_invalid_uppercase_with_repeated_chars(self):
        self.assertEqual(check_char("AA"), "Invalid")

    def test_valid_lowercase_with_repeated_chars_and_spaces(self):
        self.assertEqual(check_char("a a"), "Valid")

    def test_invalid_uppercase_with_repeated_chars_and_spaces(self):
        self.assertEqual(check_char("A A"), "Invalid")

    def test_invalid_empty_string(self):
        self.assertEqual(check_char(""), "Invalid")

    def test_invalid_single_char(self):
        self.assertEqual(check_char("a"), "Invalid")
