import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_match_found(self):
        self.assertEqual(text_match('a.*?b'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match('hello world'), 'Not matched!')

    def test_match_found_at_end(self):
        self.assertEqual(text_match('hello a.*?b world'), 'Found a match!')

    def test_match_found_at_start(self):
        self.assertEqual(text_match('a.*?b hello'), 'Found a match!')

    def test_match_found_multiple_times(self):
        self.assertEqual(text_match('a.*?b a.*?b'), 'Found a match!')

    def test_match_found_with_spaces(self):
        self.assertEqual(text_match('a.*?b   a.*?b'), 'Found a match!')

    def test_match_not_found_with_spaces(self):
        self.assertEqual(text_match('hello world   hello'), 'Not matched!')

    def test_match_found_with_newlines(self):
        self.assertEqual(text_match('a.*?b\na.*?b'), 'Found a match!')

    def test_match_not_found_with_newlines(self):
        self.assertEqual(text_match('hello world\nhello'), 'Not matched!')
