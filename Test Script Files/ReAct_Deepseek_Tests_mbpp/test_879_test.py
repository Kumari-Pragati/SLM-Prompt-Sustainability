import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match('acb'), 'Found a match!')

    def test_edge_case_no_match(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_edge_case_single_character(self):
        self.assertEqual(text_match('a'), 'Not matched!')

    def test_edge_case_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_error_case_non_string_input(self):
        with self.assertRaises(TypeError):
            text_match(123)
