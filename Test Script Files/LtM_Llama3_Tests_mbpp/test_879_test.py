import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match('a.*?b$'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match('hello world'), 'Not matched!')

    def test_empty_input(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_pattern_with_spaces(self):
        self.assertEqual(text_match('a.*?b'), 'Found a match!')

    def test_pattern_with_newlines(self):
        self.assertEqual(text_match('a.*?\nb'), 'Found a match!')

    def test_pattern_with_special_chars(self):
        self.assertEqual(text_match('a.*?b$'), 'Found a match!')

    def test_pattern_with_multiple_lines(self):
        self.assertEqual(text_match('a.*?b\na.*?b'), 'Found a match!')
