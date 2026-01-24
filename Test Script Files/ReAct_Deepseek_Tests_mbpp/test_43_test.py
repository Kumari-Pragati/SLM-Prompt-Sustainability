import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match('abc_def'), 'Found a match!')

    def test_edge_case_with_numbers(self):
        self.assertEqual(text_match('abc123_def456'), 'Found a match!')

    def test_edge_case_with_special_characters(self):
        self.assertEqual(text_match('abc_def!@#'), 'Found a match!')

    def test_edge_case_with_uppercase(self):
        self.assertEqual(text_match('ABC_DEF'), 'Not matched!')

    def test_edge_case_with_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_edge_case_with_single_word(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_edge_case_with_multiple_words(self):
        self.assertEqual(text_match('abc def'), 'Not matched!')
