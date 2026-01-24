import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_match_wordz('examplez'), 'Found a match!')
        self.assertEqual(text_match_wordz('wordzexample'), 'Found a match!')
        self.assertEqual(text_match_wordz('wordz'), 'Not matched!')

    def test_edge_cases(self):
        self.assertEqual(text_match_wordz('wordz123'), 'Not matched!')
        self.assertEqual(text_match_wordz('wordz_'), 'Not matched!')
        self.assertEqual(text_match_wordz('zword'), 'Not matched!')
        self.assertEqual(text_match_wordz('wordzZ'), 'Found a match!')
