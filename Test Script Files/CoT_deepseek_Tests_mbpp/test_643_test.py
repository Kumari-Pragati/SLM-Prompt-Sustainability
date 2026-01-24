import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_wordz_middle('hello z world'), 'Found a match!')

    def test_edge_case_no_match(self):
        self.assertEqual(text_match_wordz_middle('hello world'), 'Not matched!')

    def test_edge_case_only_z(self):
        self.assertEqual(text_match_wordz_middle('z'), 'Found a match!')

    def test_edge_case_empty_string(self):
        self.assertEqual(text_match_wordz_middle(''), 'Not matched!')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            text_match_wordz_middle(123)
