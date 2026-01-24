import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):

    def test_typical_case(self):
        patterns = ['hello', 'world']
        text = 'hello world'
        self.assertEqual(string_literals(patterns, text), 'Matched!')

    def test_no_match(self):
        patterns = ['hello', 'world']
        text = 'goodbye'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_empty_patterns(self):
        patterns = []
        text = 'hello world'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_empty_text(self):
        patterns = ['hello', 'world']
        text = ''
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_single_pattern_match(self):
        patterns = ['hello']
        text = 'hello world'
        self.assertEqual(string_literals(patterns, text), 'Matched!')

    def test_single_pattern_no_match(self):
        patterns = ['hello']
        text = 'goodbye'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_multiple_patterns_match(self):
        patterns = ['hello', 'world']
        text = 'hello world'
        self.assertEqual(string_literals(patterns, text), 'Matched!')

    def test_multiple_patterns_no_match(self):
        patterns = ['hello', 'world']
        text = 'goodbye morning'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')
