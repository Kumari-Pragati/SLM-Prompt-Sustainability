import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):
    def test_match_simple_pattern(self):
        self.assertEqual(check_literals("Hello World", "World"), 'Matched!')

    def test_match_multiple_patterns(self):
        self.assertEqual(check_literals("Python is a popular language", "Python", "language"), 'Matched!')

    def test_no_match_simple_pattern(self):
        self.assertEqual(check_literals("Hello World", "Worlds"), 'Not Matched!')

    def test_no_match_multiple_patterns(self):
        self.assertEqual(check_literals("Python is a popular language", "Ruby"), 'Not Matched!')

    def test_empty_patterns(self):
        self.assertEqual(check_literals("Test", []), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(check_literals("", ["Test"]), 'Not Matched!')

    def test_pattern_with_special_characters(self):
        self.assertEqual(check_literals("123-456-7890", r"\d+-"), 'Matched!')

    def test_case_insensitive_match(self):
        self.assertEqual(check_literals("PyThOn", "Python"), 'Matched!')
