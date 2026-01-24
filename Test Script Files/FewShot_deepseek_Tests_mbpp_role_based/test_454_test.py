import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_match_wordz('hello world'), 'Not matched!')
        self.assertEqual(text_match_wordz('hello zorld'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match_wordz(''), 'Not matched!')

    def test_boundary_case(self):
        self.assertEqual(text_match_wordz('z'), 'Found a match!')
        self.assertEqual(text_match_wordz('a' * 10000 + 'z'), 'Found a match!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match_wordz(123)
