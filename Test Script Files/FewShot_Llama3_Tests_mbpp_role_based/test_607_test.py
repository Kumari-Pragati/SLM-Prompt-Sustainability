import unittest
from mbpp_607_code import find_literals

class TestFindLiterals(unittest.TestCase):
    def test_match_found(self):
        text = 'The quick brown fox jumps over the lazy dog.'
        pattern = 'fox'
        result = find_literals(text, pattern)
        self.assertEqual(result, (pattern, 15, 19))

    def test_match_not_found(self):
        text = 'The quick brown dog jumps over the lazy dog.'
        pattern = 'fox'
        result = find_literals(text, pattern)
        self.assertIsNone(result)

    def test_pattern_empty(self):
        text = 'The quick brown fox jumps over the lazy dog.'
        pattern = ''
        result = find_literals(text, pattern)
        self.assertIsNone(result)

    def test_text_empty(self):
        text = ''
        pattern = 'fox'
        result = find_literals(text, pattern)
        self.assertIsNone(result)
