import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_wordz('hello world'), 'Not matched!')
        self.assertEqual(text_match_wordz('zorro'), 'Found a match!')
        self.assertEqual(text_match_wordz('hello zorro world'), 'Found a match!')

    def test_edge_cases(self):
        self.assertEqual(text_match_wordz(''), 'Not matched!')
        self.assertEqual(text_match_wordz('z'), 'Found a match!')
        self.assertEqual(text_match_wordz('a'*10000 + 'z'), 'Found a match!')

    def test_corner_cases(self):
        self.assertEqual(text_match_wordz('Zorro'), 'Not matched!')
        self.assertEqual(text_match_wordz('hello WORLD'), 'Not matched!')
        self.assertEqual(text_match_wordz('hello world zorro'), 'Found a match!')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            text_match_wordz(123)
        with self.assertRaises(TypeError):
            text_match_wordz(None)
