import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):
    def test_match_single_pattern(self):
        self.assertEqual(string_literals(['pattern1'], 'text containing pattern1'), 'Matched!')

    def test_match_multiple_patterns(self):
        self.assertEqual(string_literals(['pattern1', 'pattern2'], 'text containing pattern1 and pattern2'), 'Matched!')

    def test_no_match(self):
        self.assertEqual(string_literals(['pattern1'], 'text containing different pattern'), 'Not Matched!')

    def test_empty_patterns(self):
        self.assertEqual(string_literals([], 'text containing pattern'), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(string_literals(['pattern1'], ''), 'Not Matched!')
