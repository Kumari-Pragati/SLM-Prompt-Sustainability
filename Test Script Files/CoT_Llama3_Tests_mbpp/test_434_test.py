import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):
    def test_match(self):
        self.assertEqual(text_match_one('ab'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_one('abc'), 'Not matched!')

    def test_match_at_start(self):
        self.assertEqual(text_match_one('abxyz'), 'Found a match!')

    def test_match_at_end(self):
        self.assertEqual(text_match_one('xyzab'), 'Found a match!')

    def test_match_multiple(self):
        self.assertEqual(text_match_one('abab'), 'Found a match!')

    def test_no_match_multiple(self):
        self.assertEqual(text_match_one('abcabc'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_one(''), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match_one(123)
