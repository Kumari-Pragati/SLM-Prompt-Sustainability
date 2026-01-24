import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_edge_match(self):
        self.assertEqual(text_match('a'), 'Found a match!')

    def test_edge_no_match(self):
        self.assertEqual(text_match('c'), 'Not matched!')

    def test_corner_match(self):
        self.assertEqual(text_match('abab'), 'Found a match!')

    def test_corner_no_match(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match(None)
