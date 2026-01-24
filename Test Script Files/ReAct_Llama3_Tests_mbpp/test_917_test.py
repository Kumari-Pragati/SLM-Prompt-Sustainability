import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUpperLowercase(unittest.TestCase):

    def test_match(self):
        self.assertEqual(text_uppercase_lowercase('HelloWorld'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_uppercase_lowercase('hello'), 'Not matched!')

    def test_edge_case(self):
        self.assertEqual(text_uppercase_lowercase('Hello'), 'Not matched!')

    def test_edge_case2(self):
        self.assertEqual(text_uppercase_lowercase('world'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_uppercase_lowercase(''), 'Not matched!')

    def test_single_char(self):
        self.assertEqual(text_uppercase_lowercase('a'), 'Not matched!')

    def test_single_uppercase(self):
        self.assertEqual(text_uppercase_lowercase('A'), 'Not matched!')

    def test_single_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('a'), 'Not matched!')
