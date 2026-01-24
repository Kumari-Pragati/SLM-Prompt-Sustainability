import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_lowercase_underscore('hello_world'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_lowercase_underscore(''), 'Not matched!')

    def test_boundary_case(self):
        self.assertEqual(text_lowercase_underscore('a'*255 + '_' + 'a'*255), 'Found a match!')

    def test_invalid_input(self):
        self.assertEqual(text_lowercase_underscore('HelloWorld'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('hello_world123'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('hello_WORLD'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('Hello_World'), 'Not matched!')
        self.assertEqual(text_lowercase_underscore('hello_world_extra'), 'Not matched!')
