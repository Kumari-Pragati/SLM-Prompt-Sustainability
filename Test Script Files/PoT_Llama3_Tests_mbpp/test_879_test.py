import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(text_match('aabc'), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_edge_match_at_start(self):
        self.assertEqual(text_match('aabc'), 'Found a match!')

    def test_edge_match_at_end(self):
        self.assertEqual(text_match('abcba'), 'Found a match!')

    def test_edge_no_match_at_start(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_edge_no_match_at_end(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_corner_match_at_start_and_end(self):
        self.assertEqual(text_match('aabcba'), 'Found a match!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match(123)
