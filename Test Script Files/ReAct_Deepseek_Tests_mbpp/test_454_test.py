import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_wordz('examplez'), 'Found a match!')

    def test_edge_case_no_match(self):
        self.assertEqual(text_match_wordz('example'), 'Not matched!')

    def test_edge_case_only_z(self):
        self.assertEqual(text_match_wordz('z'), 'Not matched!')

    def test_edge_case_empty_string(self):
        self.assertEqual(text_match_wordz(''), 'Not matched!')

    def test_error_case_non_string_input(self):
        with self.assertRaises(TypeError):
            text_match_wordz(123)
