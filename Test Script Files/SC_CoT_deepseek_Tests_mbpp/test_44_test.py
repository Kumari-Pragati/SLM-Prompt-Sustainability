import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_string('word'), 'Found a match!')

    def test_empty_string(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_string_with_special_characters(self):
        self.assertEqual(text_match_string('word@'), 'Not matched!')

    def test_string_with_numbers(self):
        self.assertEqual(text_match_string('word123'), 'Found a match!')

    def test_string_with_whitespace(self):
        self.assertEqual(text_match_string('word '), 'Found a match!')

    def test_string_with_special_characters_and_numbers(self):
        self.assertEqual(text_match_string('word@123'), 'Not matched!')

    def test_string_with_special_characters_and_whitespace(self):
        self.assertEqual(text_match_string('word@ '), 'Not matched!')

    def test_string_with_numbers_and_whitespace(self):
        self.assertEqual(text_match_string('word 123'), 'Found a match!')

    def test_string_with_special_characters_numbers_and_whitespace(self):
        self.assertEqual(text_match_string('word@ 123'), 'Not matched!')
