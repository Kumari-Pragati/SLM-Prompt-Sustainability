import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match('a'), 'Found a match!')
        self.assertEqual(text_match('ab'), 'Found a match!')
        self.assertEqual(text_match('aba'), 'Found a match!')
        self.assertEqual(text_match('abab'), 'Found a match!')

    def test_edge_cases(self):
        self.assertEqual(text_match(''), 'Not matched!')
        self.assertEqual(text_match('a '), 'Not matched!')
        self.assertEqual(text_match('ab '), 'Found a match!')
        self.assertEqual(text_match(' ab'), 'Found a match!')
        self.assertEqual(text_match(' aba'), 'Found a match!')
        self.assertEqual(text_match('abab '), 'Found a match!')

    def test_complex_cases(self):
        self.assertEqual(text_match('ababcdab'), 'Found a match!')
        self.assertEqual(text_match('ababcdabab'), 'Found a match!')
        self.assertEqual(text_match('ababcdababcd'), 'Not matched!')
        self.assertEqual(text_match('ababcdababcdab'), 'Found a match!')
