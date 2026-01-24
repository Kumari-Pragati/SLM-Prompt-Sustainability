import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_lowercase_underscore('low_case'), 'Found a match!')

    def test_edge_case_single_word(self):
        self.assertEqual(text_lowercase_underscore('singleword'), 'Not matched!')

    def test_boundary_case_empty_string(self):
        self.assertEqual(text_lowercase_underscore(''), 'Not matched!')

    def test_corner_case_all_lowercase_with_underscore(self):
        self.assertEqual(text_lowercase_underscore('low_case_underscore'), 'Found a match!')

    def test_corner_case_all_uppercase_with_underscore(self):
        self.assertEqual(text_lowercase_underscore('UPPER_CASE_UNDERSCORE'), 'Not matched!')

    def test_corner_case_mixed_case_with_underscore(self):
        self.assertEqual(text_lowercase_underscore('MiXeD_CaSe_UndErScOrE'), 'Not matched!')

    def test_corner_case_mixed_case_without_underscore(self):
        self.assertEqual(text_lowercase_underscore('MixedCaseNoUnderscore'), 'Not matched!')
