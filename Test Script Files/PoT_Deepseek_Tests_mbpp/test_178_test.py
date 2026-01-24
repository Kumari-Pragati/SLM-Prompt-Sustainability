import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):
    def test_typical_case(self):
        patterns = ['hello', 'world']
        text = 'hello world'
        self.assertEqual(string_literals(patterns, text), 'Matched!')

    def test_edge_case_no_match(self):
        patterns = ['hello', 'world']
        text = 'no match'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_boundary_case_empty_patterns(self):
        patterns = []
        text = 'hello world'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_boundary_case_empty_text(self):
        patterns = ['hello', 'world']
        text = ''
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_corner_case_empty_pattern_and_text(self):
        patterns = []
        text = ''
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')
