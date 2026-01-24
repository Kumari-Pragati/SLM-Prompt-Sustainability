import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_match_string('hello'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_string('1234'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_special_characters(self):
        self.assertEqual(text_match_string('hello@world'), 'Found a match!')

    def test_numbers_at_start(self):
        self.assertEqual(text_match_string('123hello'), 'Found a match!')

    def test_special_characters_at_start(self):
        self.assertEqual(text_match_string('!hello'), 'Found a match!')

    def test_whitespace_only(self):
        self.assertEqual(text_match_string(' '), 'Not matched!')
