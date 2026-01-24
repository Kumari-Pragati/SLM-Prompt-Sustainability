import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match('abc_def'), 'Found a match!')

    def test_edge_case_single_word(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_edge_case_no_underscore(self):
        self.assertEqual(text_match('abc_defg'), 'Not matched!')

    def test_edge_case_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            text_match(123)
