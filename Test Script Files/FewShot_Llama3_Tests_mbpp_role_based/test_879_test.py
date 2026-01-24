import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(text_match('a.*?b$'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match('hello world'), 'Not matched!')

    def test_pattern_match(self):
        self.assertEqual(text_match('a.*?b'), 'Found a match!')

    def test_pattern_not_match(self):
        self.assertEqual(text_match('hello'), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match(123)
