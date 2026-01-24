import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):

    def test_match_string(self):
        self.assertEqual(text_match_string('Hello World'), 'Found a match!')

    def test_no_match_string(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_match_string_with_numbers(self):
        self.assertEqual(text_match_string('Hello123 World'), 'Found a match!')

    def test_no_match_string_with_punctuation(self):
        self.assertEqual(text_match_string('Hello! World'), 'Not matched!')

    def test_match_string_with_uppercase(self):
        self.assertEqual(text_match_string('HELLO WORLD'), 'Found a match!')

    def test_no_match_string_with_special_characters(self):
        self.assertEqual(text_match_string('Hello@World'), 'Not matched!')
