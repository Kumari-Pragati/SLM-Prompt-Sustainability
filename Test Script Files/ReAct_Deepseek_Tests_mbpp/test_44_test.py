import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_string('HelloWorld'), 'Found a match!')

    def test_edge_case_with_special_characters(self):
        self.assertEqual(text_match_string('Hello@World'), 'Found a match!')

    def test_edge_case_with_numbers(self):
        self.assertEqual(text_match_string('Hello123'), 'Found a match!')

    def test_edge_case_with_whitespace(self):
        self.assertEqual(text_match_string('Hello World'), 'Found a match!')

    def test_edge_case_with_empty_string(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_edge_case_with_only_special_characters(self):
        self.assertEqual(text_match_string('@#$%^&*'), 'Not matched!')

    def test_edge_case_with_only_numbers(self):
        self.assertEqual(text_match_string('1234567890'), 'Not matched!')
