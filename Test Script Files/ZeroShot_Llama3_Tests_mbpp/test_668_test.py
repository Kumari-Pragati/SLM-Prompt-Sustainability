import unittest
from mbpp_668_code import replace

class TestReplaceFunction(unittest.TestCase):

    def test_replace_single_char(self):
        self.assertEqual(replace("Hello, World!", 'o'), "Hello, World!")

    def test_replace_multiple_chars(self):
        self.assertEqual(replace("Hello, World!", 'o'), "Hello, World!")

    def test_replace_pattern(self):
        self.assertEqual(replace("Hello, Woorld!", 'o'), "Hello, World!")

    def test_replace_pattern_multiple_chars(self):
        self.assertEqual(replace("Hello, Woorld!", 'o'), "Hello, World!")

    def test_replace_pattern_no_match(self):
        self.assertEqual(replace("Hello, World!", 'o'), "Hello, World!")

    def test_replace_pattern_empty_string(self):
        self.assertEqual(replace("", 'o'), "")

    def test_replace_pattern_single_char(self):
        self.assertEqual(replace("o", 'o'), "o")

    def test_replace_pattern_multiple_chars(self):
        self.assertEqual(replace("oo", 'o'), "o")

    def test_replace_pattern_no_match_empty_string(self):
        self.assertEqual(replace("", 'o'), "")
