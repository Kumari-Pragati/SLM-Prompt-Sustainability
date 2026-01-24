import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_match(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match('cd'), 'Not matched!')

    def test_edge_case_match_at_start(self):
        self.assertEqual(text_match('abbc'), 'Found a match!')

    def test_edge_case_match_at_end(self):
        self.assertEqual(text_match('abcba'), 'Found a match!')

    def test_edge_case_no_match_at_start(self):
        self.assertEqual(text_match('cba'), 'Not matched!')

    def test_edge_case_no_match_at_end(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_edge_case_match_multiple(self):
        self.assertEqual(text_match('ababab'), 'Found a match!')

    def test_edge_case_no_match_multiple(self):
        self.assertEqual(text_match('cdcdcd'), 'Not matched!')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            text_match(123)

    def test_invalid_input_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')
