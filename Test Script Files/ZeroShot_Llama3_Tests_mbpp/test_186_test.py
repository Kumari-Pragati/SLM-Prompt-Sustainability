import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):

    def test_match(self):
        self.assertEqual(check_literals("Hello, world!", ["Hello", "world"]), 'Matched!')

    def test_no_match(self):
        self.assertEqual(check_literals("Python is awesome", ["Java", "C++"]), 'Not Matched!')

    def test_multiple_matches(self):
        self.assertEqual(check_literals("Hello, world! This is Python", ["Hello", "world", "Python"]), 'Matched!')

    def test_no_patterns(self):
        self.assertEqual(check_literals("Hello, world!", []), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(check_literals("", ["Hello", "world"]), 'Not Matched!')

    def test_empty_patterns(self):
        self.assertEqual(check_literals("Hello, world!", []), 'Not Matched!')
