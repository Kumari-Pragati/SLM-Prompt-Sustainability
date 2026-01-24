import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):
    def test_simple_match(self):
        patterns = ['test']
        text = 'This is a test'
        self.assertEqual(string_literals(patterns, text), 'Matched!')

    def test_simple_no_match(self):
        patterns = ['test']
        text = 'This is not a test'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_multiple_patterns_match(self):
        patterns = ['test', 'example']
        text = 'This is a test'
        self.assertEqual(string_literals(patterns, text), 'Matched!')

    def test_multiple_patterns_no_match(self):
        patterns = ['test', 'example']
        text = 'This is not a test or example'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_empty_patterns(self):
        patterns = []
        text = 'This is a test'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_empty_text(self):
        patterns = ['test']
        text = ''
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_empty_both(self):
        patterns = []
        text = ''
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')
