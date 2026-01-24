import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_edge_case(self):
        self.assertEqual(text_match('a'), 'Found a match!')

    def test_pattern_match(self):
        self.assertEqual(text_match('ab*?'), 'Found a match!')

    def test_pattern_no_match(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match(None)
