import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_lowercase_underscore('a_b'), 'Found a match!')

    def test_edge_condition_empty_string(self):
        self.assertEqual(text_lowercase_underscore(''), 'Not matched!')

    def test_edge_condition_single_word(self):
        self.assertEqual(text_lowercase_underscore('word'), 'Not matched!')

    def test_boundary_condition_single_underscore(self):
        self.assertEqual(text_lowercase_underscore('_'), 'Not matched!')

    def test_complex_case_multiple_words(self):
        self.assertEqual(text_lowercase_underscore('a_b_c_d'), 'Not matched!')

    def test_complex_case_mixed_case(self):
        self.assertEqual(text_lowercase_underscore('A_b'), 'Not matched!')

    def test_complex_case_numbers(self):
        self.assertEqual(text_lowercase_underscore('a1_b2'), 'Not matched!')
