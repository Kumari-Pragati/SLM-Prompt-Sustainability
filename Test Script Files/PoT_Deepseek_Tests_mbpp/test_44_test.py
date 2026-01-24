import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_string('HelloWorld'), 'Found a match!')

    def test_edge_case_single_word(self):
        self.assertEqual(text_match_string('Python'), 'Found a match!')

    def test_boundary_case_empty_string(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_corner_case_whitespace_only(self):
        self.assertEqual(text_match_string(' '), 'Not matched!')

    def test_corner_case_special_characters(self):
        self.assertEqual(text_match_string('!@#$%^&*()'), 'Found a match!')

    def test_corner_case_numbers(self):
        self.assertEqual(text_match_string('123456'), 'Found a match!')
