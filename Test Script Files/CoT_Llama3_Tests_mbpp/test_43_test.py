import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_match(self):
        self.assertEqual(text_match('hello_world'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match('hello'), 'Not matched!')

    def test_match_with_spaces(self):
        self.assertEqual(text_match('hello world'), 'Not matched!')

    def test_match_with_uppercase(self):
        self.assertEqual(text_match('Hello_World'), 'Found a match!')

    def test_match_with_numbers(self):
        self.assertEqual(text_match('hello123_world'), 'Found a match!')

    def test_match_with_special_chars(self):
        self.assertEqual(text_match('hello!_world'), 'Found a match!')

    def test_no_match_with_special_chars(self):
        self.assertEqual(text_match('hello!'), 'Not matched!')

    def test_no_match_with_punctuation(self):
        self.assertEqual(text_match('hello.'), 'Not matched!')

    def test_no_match_with_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')
