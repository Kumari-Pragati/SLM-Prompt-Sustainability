import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):

    def test_single_lowercase_letter(self):
        self.assertEqual(check_char('a'), "Valid")

    def test_multiple_lowercase_letters(self):
        self.assertEqual(check_char('abcba'), "Valid")

    def test_uppercase_letter(self):
        self.assertEqual(check_char('A'), "Invalid")

    def test_number(self):
        self.assertEqual(check_char('1'), "Invalid")

    def test_special_character(self):
        self.assertEqual(check_char('@'), "Invalid")

    def test_empty_string(self):
        self.assertEqual(check_char(''), "Invalid")

    def test_string_with_spaces(self):
        self.assertEqual(check_char('a b'), "Invalid")

    def test_string_with_non_repeated_characters(self):
        self.assertEqual(check_char('abcd'), "Invalid")
