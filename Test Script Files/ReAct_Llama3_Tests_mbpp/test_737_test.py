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
        self.assertEqual(check_str("bcd"), "Invalid")

    def test_string_starting_with_digit(self):
        self.assertEqual(check_str("123"), "Invalid")

    def test_string_starting_with_underscore(self):
        self.assertEqual(check_str("_hello"), "Valid")

    def test_empty_string(self):
        self.assertEqual(check_str(""), "Invalid")

    def test_string_with_spaces(self):
        self.assertEqual(check_str("hello world"), "Invalid")

    def test_string_with_punctuation(self):
        self.assertEqual(check_str("hello!"), "Invalid")

    def test_string_with_special_characters(self):
        self.assertEqual(check_str("hello@world"), "Invalid")
