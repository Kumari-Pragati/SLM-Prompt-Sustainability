import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match('xyz'), 'Not matched!')

    def test_match_found_at_start(self):
        self.assertEqual(text_match('abxyz'), 'Found a match!')

    def test_match_found_at_end(self):
        self.assertEqual(text_match('xyzab'), 'Found a match!')

    def test_match_found_multiple_times(self):
        self.assertEqual(text_match('abab'), 'Found a match!')

    def test_match_found_at_start_and_end(self):
        self.assertEqual(text_match('abxyzab'), 'Found a match!')

    def test_match_not_found_at_all(self):
        self.assertEqual(text_match('123'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_no_match(self):
        self.assertEqual(text_match('abc'), 'Not matched!')
