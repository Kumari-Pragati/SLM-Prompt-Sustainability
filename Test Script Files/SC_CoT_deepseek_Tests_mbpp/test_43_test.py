import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match('abc_def'), 'Found a match!')

    def test_edge_case_single_word(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_edge_case_single_underscore(self):
        self.assertEqual(text_match('_abc_def'), 'Not matched!')

    def test_edge_case_multiple_underscores(self):
        self.assertEqual(text_match('abc_def_ghi'), 'Not matched!')

    def test_special_case_uppercase(self):
        self.assertEqual(text_match('ABC_DEF'), 'Not matched!')

    def test_special_case_numbers(self):
        self.assertEqual(text_match('abc1_def2'), 'Not matched!')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            text_match(123)
