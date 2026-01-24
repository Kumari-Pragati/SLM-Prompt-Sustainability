import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):
    def test_typical_use_case(self):
        patterns = ['hello', 'world']
        text = 'hello world'
        self.assertEqual(string_literals(patterns, text), 'Matched!')

    def test_edge_case(self):
        patterns = ['hello', 'world']
        text = 'goodbye'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_boundary_case(self):
        patterns = ['']
        text = 'hello world'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_invalid_input(self):
        patterns = ['hello', 123]
        text = 'hello world'
        with self.assertRaises(TypeError):
            string_literals(patterns, text)
