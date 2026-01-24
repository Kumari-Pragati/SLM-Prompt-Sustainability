import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(text_lowercase_underscore('hello_world'), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_lowercase_underscore('hello world'), 'Not matched!')

    def test_edge_match_at_start(self):
        self.assertEqual(text_lowercase_underscore('a_b'), 'Found a match!')

    def test_edge_match_at_end(self):
        self.assertEqual(text_lowercase_underscore('a_b_c'), 'Found a match!')

    def test_edge_no_match_at_start(self):
        self.assertEqual(text_lowercase_underscore('Hello_world'), 'Not matched!')

    def test_edge_no_match_at_end(self):
        self.assertEqual(text_lowercase_underscore('a_b_c_d'), 'Not matched!')

    def test_corner_match_with_multiple_underscores(self):
        self.assertEqual(text_lowercase_underscore('hello_world_again'), 'Found a match!')

    def test_corner_no_match_with_non_alphabetic_characters(self):
        self.assertEqual(text_lowercase_underscore('hello!world'), 'Not matched!')
