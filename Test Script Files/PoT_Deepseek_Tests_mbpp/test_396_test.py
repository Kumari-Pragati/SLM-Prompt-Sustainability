import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):

    def test_single_lowercase_letter(self):
        self.assertEqual(check_char('a'), "Valid")

    def test_multiple_lowercase_letters(self):
        self.assertEqual(check_char('abc'), "Valid")

    def test_lowercase_letter_with_special_characters(self):
        self.assertEqual(check_char('a@'), "Invalid")

    def test_lowercase_letter_with_numbers(self):
        self.assertEqual(check_char('a1'), "Invalid")

    def test_lowercase_letter_with_uppercase(self):
        self.assertEqual(check_char('A'), "Invalid")

    def test_empty_string(self):
        self.assertEqual(check_char(''), "Invalid")

    def test_single_uppercase_letter(self):
        self.assertEqual(check_char('A'), "Invalid")

    def test_single_number(self):
        self.assertEqual(check_char('1'), "Invalid")

    def test_special_characters(self):
        self.assertEqual(check_char('@#$'), "Invalid")

    def test_whitespace(self):
        self.assertEqual(check_char(' '), "Invalid")
