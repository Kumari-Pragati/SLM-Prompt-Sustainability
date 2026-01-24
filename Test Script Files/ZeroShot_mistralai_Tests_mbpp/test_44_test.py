import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_single_word(self):
        self.assertEqual(text_match_string('Hello'), 'Found a match!')

    def test_multiple_words(self):
        self.assertEqual(text_match_string('Hello World'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_string('12345'), 'Not matched!')

    def test_special_characters(self):
        self.assertEqual(text_match_string('Hello@World'), 'Not matched!')

    def test_numbers(self):
        self.assertEqual(text_match_string('123Hello'), 'Found a match!')
