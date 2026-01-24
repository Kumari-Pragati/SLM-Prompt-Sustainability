import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):

    def test_valid_single_char(self):
        self.assertEqual(check_char('a'), "Valid")

    def test_valid_multiple_chars(self):
        self.assertEqual(check_char('abc'), "Invalid")

    def test_valid_repeating_chars(self):
        self.assertEqual(check_char('aa'), "Valid")

    def test_invalid_chars(self):
        self.assertEqual(check_char('A'), "Invalid")

    def test_invalid_chars_multiple(self):
        self.assertEqual(check_char('abc123'), "Invalid")

    def test_empty_string(self):
        self.assertEqual(check_char(''), "Invalid")

    def test_single_digit(self):
        self.assertEqual(check_char('1'), "Invalid")

    def test_single_uppercase(self):
        self.assertEqual(check_char('A'), "Invalid")

    def test_single_punctuation(self):
        self.assertEqual(check_char('.'), "Invalid")

    def test_single_space(self):
        self.assertEqual(check_char(' '), "Invalid")
