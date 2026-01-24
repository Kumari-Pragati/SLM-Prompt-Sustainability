import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):
    def test_typical_case(self):
        patterns = ['hello', 'world']
        text = 'hello world'
        self.assertEqual(string_literals(patterns, text), 'Matched!')

    def test_edge_case(self):
        patterns = ['hello', 'world']
        text = ''
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_boundary_case(self):
        patterns = ['hello', 'world']
        text = 'hello'
        self.assertEqual(string_literals(patterns, text), 'Matched!')

    def test_corner_case(self):
        patterns = ['hello', 'world']
        text = 'goodbye world'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_invalid_input(self):
        patterns = ['hello', 'world']
        text = 12345
        with self.assertRaises(TypeError):
            string_literals(patterns, text)
