import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUppercaseLowercase(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_uppercase_lowercase('Abc'), 'Found a match!')

    def test_edge_case_empty_string(self):
        self.assertEqual(text_uppercase_lowercase(''), 'Not matched!')

    def test_boundary_case_single_character(self):
        self.assertEqual(text_uppercase_lowercase('A'), 'Not matched!')

    def test_complex_case_no_uppercase_after_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('abc'), 'Not matched!')

    def test_complex_case_no_lowercase_after_uppercase(self):
        self.assertEqual(text_uppercase_lowercase('ABC'), 'Not matched!')

    def test_complex_case_multiple_uppercase_and_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('AbCdEfGhI'), 'Found a match!')
