import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):
    def test_single_lowercase_letter(self):
        self.assertEqual(check_char('a'), "Valid")

    def test_multiple_lowercase_letters(self):
        self.assertEqual(check_char('abcba'), "Valid")

    def test_single_uppercase_letter(self):
        self.assertEqual(check_char('A'), "Invalid")

    def test_multiple_uppercase_letters(self):
        self.assertEqual(check_char('AbcBa'), "Invalid")

    def test_number(self):
        self.assertEqual(check_char('1'), "Invalid")

    def test_special_character(self):
        self.assertEqual(check_char('@'), "Invalid")

    def test_empty_string(self):
        self.assertEqual(check_char(''), "Invalid")

    def test_long_string(self):
        self.assertEqual(check_char('abcdefg'), "Invalid")
