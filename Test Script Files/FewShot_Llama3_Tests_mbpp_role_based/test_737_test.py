import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):
    def test_valid_string(self):
        self.assertEqual(check_str("Hello"), "Valid")

    def test_invalid_string(self):
        self.assertEqual(check_str("123"), "Invalid")

    def test_string_starting_with_vowel(self):
        self.assertEqual(check_str("aeiou"), "Valid")

    def test_string_starting_with_consonant(self):
        self.assertEqual(check_str("bcdf"), "Invalid")

    def test_string_with_non_alphanumeric_characters(self):
        self.assertEqual(check_str("aeiou!"), "Valid")

    def test_string_with_spaces(self):
        self.assertEqual(check_str("aeiou "), "Valid")

    def test_empty_string(self):
        self.assertEqual(check_str(""), "Invalid")
