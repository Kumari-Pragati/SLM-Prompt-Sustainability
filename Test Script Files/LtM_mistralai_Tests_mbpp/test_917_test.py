import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUppercaseLowercase(unittest.TestCase):

    def test_simple_uppercase(self):
        self.assertEqual(text_uppercase_lowercase('ABC'), 'Found a match!')

    def test_simple_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('abc'), 'Found a match!')

    def test_mixed_case(self):
        self.assertEqual(text_uppercase_lowercase('AbCd'), 'Found a match!')

    def test_edge_case_empty_string(self):
        self.assertEqual(text_uppercase_lowercase(''), 'Not matched!')

    def test_edge_case_single_uppercase(self):
        self.assertEqual(text_uppercase_lowercase('A'), 'Not matched!')

    def test_edge_case_single_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('a'), 'Not matched!')

    def test_edge_case_no_match(self):
        self.assertEqual(text_uppercase_lowercase('123'), 'Not matched!')
