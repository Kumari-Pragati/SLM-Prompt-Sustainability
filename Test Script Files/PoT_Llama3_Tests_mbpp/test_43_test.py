import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(text_match('hello_world'), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match('hello'), 'Not matched!')

    def test_edge_match(self):
        self.assertEqual(text_match('abc_def'), 'Found a match!')

    def test_edge_no_match(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_corner_match(self):
        self.assertEqual(text_match('_hello_world'), 'Found a match!')

    def test_corner_no_match(self):
        self.assertEqual(text_match('_hello'), 'Not matched!')
