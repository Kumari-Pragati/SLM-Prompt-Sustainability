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

    def test_pattern_with_special_characters(self):
        self.assertEqual(string_literals(['.\\*\\+', 'pattern'], 'text.containing.*pattern'), 'Matched!')

    def test_invalid_input_type(self):
        self.assertRaises(TypeError, string_literals, [1, 2], 'text')
