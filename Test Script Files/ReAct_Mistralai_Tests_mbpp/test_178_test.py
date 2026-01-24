import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):

    def test_matches_single_pattern(self):
        self.assertEqual(string_literals(['pattern'], 'text containing pattern'), 'Matched!')

    def test_matches_multiple_patterns(self):
        self.assertEqual(string_literals(['pattern1', 'pattern2'], 'text containing pattern1 and pattern2'), 'Matched!')

    def test_no_matches(self):
        self.assertEqual(string_literals(['pattern'], 'text not containing pattern'), 'Not Matched!')

    def test_empty_patterns(self):
        self.assertEqual(string_literals([], 'text'), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(string_literals(['pattern'], ''), 'Not Matched!')

    def test_pattern_with_spaces(self):
        self.assertEqual(string_literals(['pattern with spaces'], 'text containing pattern with spaces'), 'Matched!')

    def test_case_insensitive_match(self):
        self.assertEqual(string_literals(['PATTERN'], 'text containing PATTERN'), 'Matched!')

    def test_escaped_pattern(self):
        self.assertEqual(string_literals(['\\.\\+'], 'text.more.text'), 'Matched!')

    def test_error_invalid_pattern(self):
        self.assertRaises(Exception, string_literals, ['invalid_pattern'], 'text')
