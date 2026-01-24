import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):

    def test_match(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world'), 'Matched!')

    def test_not_match(self):
        self.assertEqual(string_literals(['hello', 'world'], 'goodbye'), 'Not Matched!')

    def test_multiple_matches(self):
        self.assertEqual(string_literals(['hello', 'world', 'python'], 'hello world python'), 'Matched!')

    def test_no_matches(self):
        self.assertEqual(string_literals(['hello', 'world'], ''), 'Not Matched!')

    def test_empty_pattern(self):
        self.assertEqual(string_literals(['', 'world'], 'hello world'), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(string_literals(['hello', ''], '',), 'Not Matched!')
