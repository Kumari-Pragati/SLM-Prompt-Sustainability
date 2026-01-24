import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):
    def test_match_found(self):
        patterns = ['hello', 'world']
        text = 'hello world'
        self.assertEqual(string_literals(patterns, text), 'Matched!')

    def test_match_not_found(self):
        patterns = ['hello', 'world']
        text = 'foo bar'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_empty_patterns(self):
        patterns = []
        text = 'hello world'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_empty_text(self):
        patterns = ['hello', 'world']
        text = ''
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_multiple_matches(self):
        patterns = ['hello', 'world', 'foo']
        text = 'hello world foo'
        self.assertEqual(string_literals(patterns, text), 'Matched!')

    def test_no_patterns(self):
        patterns = []
        text = 'hello world'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')
