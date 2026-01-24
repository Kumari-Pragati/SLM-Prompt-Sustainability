import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_match('example_name'), 'Found a match!')

    def test_edge_case_lowercase(self):
        self.assertEqual(text_match('example_name_'), 'Not matched!')

    def test_edge_case_uppercase(self):
        self.assertEqual(text_match('EXAMPLE_NAME'), 'Not matched!')

    def test_edge_case_special_characters(self):
        self.assertEqual(text_match('example_#_name'), 'Not matched!')

    def test_edge_case_numbers(self):
        self.assertEqual(text_match('example1_name'), 'Not matched!')
        self.assertEqual(text_match('example_name1'), 'Not matched!')
        self.assertEqual(text_match('example_name_1'), 'Not matched!')

    def test_corner_case_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_corner_case_whitespace(self):
        self.assertEqual(text_match('   example_name   '), 'Not matched!')

    def test_corner_case_multiple_underscores(self):
        self.assertEqual(text_match('example___name'), 'Not matched!')
