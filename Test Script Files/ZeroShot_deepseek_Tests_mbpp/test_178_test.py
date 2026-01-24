import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):

    def test_matched_pattern(self):
        patterns = ['hello', 'world']
        text = 'hello world'
        self.assertEqual(string_literals(patterns, text), 'Matched!')

    def test_unmatched_pattern(self):
        patterns = ['hello', 'world']
        text = 'goodbye world'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_empty_pattern(self):
        patterns = []
        text = 'hello world'
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')

    def test_empty_text(self):
        patterns = ['hello', 'world']
        text = ''
        self.assertEqual(string_literals(patterns, text), 'Not Matched!')
