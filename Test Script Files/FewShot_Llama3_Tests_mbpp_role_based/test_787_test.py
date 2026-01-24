import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(text_match_three('ababab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match_three('hello'), 'Not matched!')

    def test_match_found_at_start(self):
        self.assertEqual(text_match_three('abababhello'), 'Found a match!')

    def test_match_found_at_end(self):
        self.assertEqual(text_match_three('helloababab'), 'Found a match!')

    def test_match_found_multiple_times(self):
        self.assertEqual(text_match_three('abababababab'), 'Found a match!')

    def test_match_found_with_spaces(self):
        self.assertEqual(text_match_three(' ab ab ab ab '), 'Found a match!')

    def test_match_found_with_punctuation(self):
        self.assertEqual(text_match_three('ab,ab,ab,ab'), 'Found a match!')
