import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):
    def test_valid_string_start_with_vowel(self):
        self.assertEqual(check_str('a123_'), "Valid")
        self.assertEqual(check_str('A456_'), "Valid")

    def test_valid_string_contains_alphanumeric_and_underscore(self):
        self.assertEqual(check_str('a737_code'), "Valid")
        self.assertEqual(check_str('A737_code'), "Valid")
        self.assertEqual(check_str('a737_code123'), "Valid")
        self.assertEqual(check_str('A737_code123'), "Valid")

    def test_invalid_string_start_with_consonant(self):
        self.assertEqual(check_str('b123_'), "Invalid")
        self.assertEqual(check_str('B123_'), "Invalid")

    def test_empty_string(self):
        self.assertEqual(check_str(''), "Invalid")

    def test_string_with_special_characters(self):
        self.assertEqual(check_str('a737@code'), "Invalid")
        self.assertEqual(check_str('A737#code'), "Invalid")
