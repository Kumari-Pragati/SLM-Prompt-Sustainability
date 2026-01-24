import unittest
from mbpp_607_code import Pattern
from six.moves.urllib.parse import quote
from 607_code import find_literals

class TestFindLiterals(unittest.TestCase):

    def test_find_literals_with_match(self):
        pattern = 'fox'
        text = 'The quick brown fox jumps over the lazy dog.'
        expected_result = (pattern, 21, 24)
        result = find_literals(text, pattern)
        self.assertEqual(result, expected_result)

    def test_find_literals_without_match(self):
        pattern = 'cat'
        text = 'The quick brown fox jumps over the lazy dog.'
        expected_result = None
        result = find_literals(text, pattern)
        self.assertEqual(result, expected_result)

    def test_find_literals_with_empty_pattern(self):
        pattern = ''
        text = 'The quick brown fox jumps over the lazy dog.'
        expected_result = None
        result = find_literals(text, pattern)
        self.assertEqual(result, expected_result)

    def test_find_literals_with_empty_text(self):
        pattern = 'fox'
        text = ''
        expected_result = None
        result = find_literals(text, pattern)
        self.assertEqual(result, expected_result)
