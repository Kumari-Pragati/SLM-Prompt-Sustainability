import unittest
from mbpp_607_code import find_literals

class TestFindLiterals(unittest.TestCase):

    def test_typical_case(self):
        pattern = 'fox'
        text = 'The quick brown fox jumps over the lazy dog.'
        result = find_literals(text, pattern)
        self.assertEqual(result, ('fox', 16, 19))

    def test_edge_case_no_match(self):
        pattern = 'fox'
        text = 'The quick brown dog jumps over the lazy cat.'
        result = find_literals(text, pattern)
        self.assertIsNone(result)

    def test_edge_case_empty_pattern(self):
        pattern = ''
        text = 'The quick brown fox jumps over the lazy dog.'
        result = find_literals(text, pattern)
        self.assertIsNone(result)

    def test_edge_case_empty_text(self):
        pattern = 'fox'
        text = ''
        result = find_literals(text, pattern)
        self.assertIsNone(result)

    def test_edge_case_pattern_longer_than_text(self):
        pattern = 'fox jumps over the lazy dog.'
        text = 'The quick brown fox'
        result = find_literals(text, pattern)
        self.assertIsNone(result)

    def test_edge_case_pattern_not_in_text(self):
        pattern = 'fox'
        text = 'The quick brown dog jumps over the lazy cat.'
        result = find_literals(text, pattern)
        self.assertIsNone(result)
