import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(text_match_wordz('hello world'), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match_wordz('hello'), 'Not matched!')

    def test_edge_case_match(self):
        self.assertEqual(text_match_wordz('zoo'), 'Found a match!')

    def test_edge_case_no_match(self):
        self.assertEqual(text_match_wordz(''), 'Not matched!')

    def test_edge_case_empty_string(self):
        self.assertEqual(text_match_wordz(''), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match_wordz(None)

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            text_match_wordz(123)

    def test_invalid_input_non_string_list(self):
        with self.assertRaises(TypeError):
            text_match_wordz(['hello', 'world'])
