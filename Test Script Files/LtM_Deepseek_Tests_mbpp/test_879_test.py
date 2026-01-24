import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_match('acb'), 'Found a match!')

    def test_edge_case_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_boundary_case_single_characters(self):
        self.assertEqual(text_match('ab'), 'Not matched!')
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('b'), 'Not matched!')

    def test_complex_case_multiple_characters(self):
        self.assertEqual(text_match('abc'), 'Found a match!')
        self.assertEqual(text_match('aab'), 'Not matched!')
        self.assertEqual(text_match('abb'), 'Not matched!')

    def test_edge_case_special_characters(self):
        self.assertEqual(text_match('a!@#$%^&*()b'), 'Found a match!')

    def test_complex_case_numbers(self):
        self.assertEqual(text_match('a123b'), 'Found a match!')
        self.assertEqual(text_match('a1b'), 'Not matched!')
