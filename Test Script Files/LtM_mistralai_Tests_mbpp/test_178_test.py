import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(string_literals(['abc'], 'abcdefgabc'), 'Matched!')

    def test_case_insensitive_match(self):
        self.assertEqual(string_literals(['AbC'], 'abcdefgAbC'), 'Matched!')

    def test_multiple_matches(self):
        self.assertEqual(string_literals(['abc', 'def'], 'abcdefg'), 'Matched!')

    def test_no_match(self):
        self.assertEqual(string_literals(['abc'], '123456'), 'Not Matched!')

    def test_empty_patterns(self):
        self.assertEqual(string_literals([]), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(string_literals(['abc'], ''), 'Not Matched!')

    def test_pattern_with_special_characters(self):
        self.assertEqual(string_literals(['[a-z]'], 'abcdefg'), 'Matched!')
