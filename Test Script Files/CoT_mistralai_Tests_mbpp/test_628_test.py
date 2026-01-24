import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(replace_spaces(""), "")

    def test_single_space(self):
        self.assertEqual(replace_spaces(" a "), "%02")

    def test_multiple_spaces(self):
        self.assertEqual(replace_spaces("hello world"), "h%02e%02l%02l%02o%02  %02w%02o%02r%02l%02d")

    def test_long_string(self):
        long_string = "a" * 1001
        self.assertEqual(replace_spaces(long_string), -1)

    def test_string_with_only_spaces(self):
        self.assertEqual(replace_spaces("   "), "%02%02%02")

    def test_string_with_special_characters(self):
        self.assertEqual(replace_spaces("hello%world"), "h%02e%02l%02l%02o%02l%02d")

    def test_string_with_numbers(self):
        self.assertEqual(replace_spaces("123 456"), "123%02  %02456")

    def test_string_with_long_words(self):
        long_word = "antidisestablishmentarianism"
        self.assertEqual(replace_spaces(long_word), f"a%02n{long_word[1:].replace(' ', '%02')}%02m")
