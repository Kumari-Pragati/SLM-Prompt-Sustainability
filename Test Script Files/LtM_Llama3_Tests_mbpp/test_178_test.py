import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(string_literals(['hello'], 'hello world'), 'Matched!')

    def test_simple_no_match(self):
        self.assertEqual(string_literals(['hello'], 'goodbye'), 'Not Matched!')

    def test_empty_pattern(self):
        self.assertEqual(string_literals([], 'hello'), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(string_literals(['hello'], ''), 'Not Matched!')

    def test_multiple_matches(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world'), 'Matched!')

    def test_no_matches(self):
        self.assertEqual(string_literals(['hello', 'world'], 'foo'), 'Not Matched!')

    def test_pattern_with_spaces(self):
        self.assertEqual(string_literals(['hello world'], 'hello world'), 'Matched!')

    def test_text_with_spaces(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world'), 'Matched!')

    def test_pattern_with_special_chars(self):
        self.assertEqual(string_literals(['hello*'], 'hello*'), 'Matched!')

    def test_text_with_special_chars(self):
        self.assertEqual(string_literals(['hello*'], 'hello*'), 'Matched!')
