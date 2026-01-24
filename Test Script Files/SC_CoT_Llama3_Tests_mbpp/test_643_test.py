import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):

    def test_typical_match(self):
        self.assertEqual(text_match_wordz_middle("wordz"), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match_wordz_middle("word"), 'Not matched!')

    def test_edge_wordz_at_start(self):
        self.assertEqual(text_match_wordz_middle("zwordz"), 'Found a match!')

    def test_edge_wordz_at_end(self):
        self.assertEqual(text_match_wordz_middle("wordzword"), 'Found a match!')

    def test_edge_wordz_in_middle(self):
        self.assertEqual(text_match_wordz_middle("wordwordz"), 'Found a match!')

    def test_edge_wordz_at_start_and_end(self):
        self.assertEqual(text_match_wordz_middle("zwordzword"), 'Found a match!')

    def test_edge_wordz_at_start_and_middle(self):
        self.assertEqual(text_match_wordz_middle("zwordwordz"), 'Found a match!')

    def test_edge_wordz_at_end_and_middle(self):
        self.assertEqual(text_match_wordz_middle("wordzwordz"), 'Found a match!')

    def test_edge_wordz_at_start_and_end_and_middle(self):
        self.assertEqual(text_match_wordz_middle("zwordzwordz"), 'Found a match!')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            text_match_wordz_middle(123)

    def test_invalid_input_empty_string(self):
        self.assertEqual(text_match_wordz_middle(""), 'Not matched!')
