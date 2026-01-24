import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):

    def test_typical_match(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world'), 'Matched!')

    def test_typical_no_match(self):
        self.assertEqual(string_literals(['hello', 'world'], 'foo bar'), 'Not Matched!')

    def test_edge_match_at_start(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello foo bar'), 'Matched!')

    def test_edge_match_at_end(self):
        self.assertEqual(string_literals(['hello', 'world'], 'foo bar world'), 'Matched!')

    def test_edge_match_at_middle(self):
        self.assertEqual(string_literals(['hello', 'world'], 'foo hello bar world'), 'Matched!')

    def test_edge_no_match_at_start(self):
        self.assertEqual(string_literals(['hello', 'world'], 'foo bar world'), 'Not Matched!')

    def test_edge_no_match_at_end(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world foo'), 'Not Matched!')

    def test_edge_no_match_at_middle(self):
        self.assertEqual(string_literals(['hello', 'world'], 'foo hello foo world'), 'Not Matched!')

    def test_multiple_patterns_match(self):
        self.assertEqual(string_literals(['hello', 'world', 'foo'], 'hello world foo bar'), 'Matched!')

    def test_multiple_patterns_no_match(self):
        self.assertEqual(string_literals(['hello', 'world', 'foo'], 'bar baz'), 'Not Matched!')

    def test_empty_patterns(self):
        self.assertEqual(string_literals([], 'hello world'), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(string_literals(['hello', 'world'], ''), 'Not Matched!')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            string_literals('hello', 'world')

    def test_invalid_input_type_pattern(self):
        with self.assertRaises(TypeError):
            string_literals([1, 2], 'world')

    def test_invalid_input_type_text(self):
        with self.assertRaises(TypeError):
            string_literals(['hello', 'world'], 1)
