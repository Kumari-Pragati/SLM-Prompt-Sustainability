import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(check_literals("Hello, world!", ["world"]), 'Matched!')

    def test_simple_no_match(self):
        self.assertEqual(check_literals("Hello, world!", ["universe"]), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(check_literals("", ["world"]), 'Not Matched!')

    def test_empty_pattern(self):
        self.assertEqual(check_literals("Hello, world!", []), 'Not Matched!')

    def test_match_at_start(self):
        self.assertEqual(check_literals("world, hello!", ["world"]), 'Matched!')

    def test_match_at_end(self):
        self.assertEqual(check_literals("hello, world!", ["world"]), 'Matched!')

    def test_multiple_patterns(self):
        self.assertEqual(check_literals("Hello, world!", ["world", "hello"]), 'Matched!')

    def test_multiple_patterns_no_match(self):
        self.assertEqual(check_literals("Hello, universe!", ["world", "hello"]), 'Not Matched!')

    def test_pattern_with_special_chars(self):
        self.assertEqual(check_literals("Hello, world!", [r"\bworld\b"]), 'Matched!')

    def test_pattern_with_special_chars_no_match(self):
        self.assertEqual(check_literals("Hello, universe!", [r"\bworld\b"]), 'Not Matched!')
