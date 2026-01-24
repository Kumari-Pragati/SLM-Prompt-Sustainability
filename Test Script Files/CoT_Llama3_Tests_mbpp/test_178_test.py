import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):
    def test_match(self):
        self.assertEqual(string_literals(['hello'], 'hello world'), 'Matched!')

    def test_no_match(self):
        self.assertEqual(string_literals(['hello'], 'goodbye'), 'Not Matched!')

    def test_multiple_matches(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world'), 'Matched!')

    def test_no_patterns(self):
        self.assertEqual(string_literals([], 'hello'), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(string_literals(['hello'], ''), 'Not Matched!')

    def test_empty_pattern(self):
        self.assertEqual(string_literals([''], 'hello'), 'Not Matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            string_literals(None, 'hello')
