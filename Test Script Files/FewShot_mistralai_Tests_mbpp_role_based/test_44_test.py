import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):
    def test_found_match_with_word(self):
        self.assertEqual(text_match_string("HelloWorld"), 'Found a match!')

    def test_not_found_match_with_number(self):
        self.assertEqual(text_match_string("12345"), 'Not matched!')

    def test_found_match_with_empty_string(self):
        self.assertEqual(text_match_string(""), 'Not matched!')

    def test_found_match_with_whitespace(self):
        self.assertEqual(text_match_string("   "), 'Not matched!')

    def test_found_match_with_special_characters(self):
        self.assertEqual(text_match_string("@#$%^&*()_+-="), 'Not matched!')
