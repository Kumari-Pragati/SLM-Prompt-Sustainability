import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(text_lowercase_underscore('hello_world'), 'Found a match!')

    def test_edge_condition(self):
        self.assertEqual(text_lowercase_underscore(''), 'Not matched!')

    def test_boundary_condition(self):
        self.assertEqual(text_lowercase_underscore('a_b'), 'Found a match!')
        self.assertEqual(text_lowercase_underscore('a_b_c'), 'Not matched!')

    def test_invalid_input(self):
        self.assertEqual(text_lowercase_underscore('HelloWorld'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('hello_WORLD'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('123_456'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('hello_world123'), 'Not matched!')
