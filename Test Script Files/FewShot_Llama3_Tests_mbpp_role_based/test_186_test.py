import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):
    def test_match_found(self):
        text = "Hello, world!"
        patterns = ["Hello", "world"]
        self.assertEqual(check_literals(text, patterns), 'Matched!')

    def test_match_not_found(self):
        text = "Hello, world!"
        patterns = ["Python", "Java"]
        self.assertEqual(check_literals(text, patterns), 'Not Matched!')

    def test_empty_text(self):
        text = ""
        patterns = ["Hello", "world"]
        self.assertEqual(check_literals(text, patterns), 'Not Matched!')

    def test_empty_patterns(self):
        text = "Hello, world!"
        patterns = []
        self.assertEqual(check_literals(text, patterns), 'Not Matched!')

    def test_single_pattern_match(self):
        text = "Hello, world!"
        patterns = ["Hello"]
        self.assertEqual(check_literals(text, patterns), 'Matched!')

    def test_single_pattern_no_match(self):
        text = "Python is awesome!"
        patterns = ["Java"]
        self.assertEqual(check_literals(text, patterns), 'Not Matched!')
