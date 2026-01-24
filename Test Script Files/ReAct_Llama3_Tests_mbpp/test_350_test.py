import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(minimum_Length(""), 0)

    def test_single_character_string(self):
        self.assertEqual(minimum_Length("a"), 1)

    def test_all_same_characters_string(self):
        self.assertEqual(minimum_Length("aaab"), 2)

    def test_all_different_characters_string(self):
        self.assertEqual(minimum_Length("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_long_string(self):
        self.assertEqual(minimum_Length("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"), 26)

    def test_string_with_spaces(self):
        self.assertEqual(minimum_Length("a b c"), 1)

    def test_string_with_punctuation(self):
        self.assertEqual(minimum_Length("a, b! c?"), 1)

    def test_string_with_numbers(self):
        self.assertEqual(minimum_Length("a1 b2 c3"), 1)

    def test_string_with_special_characters(self):
        self.assertEqual(minimum_Length("a@ b# c$"), 1)

    def test_string_with_newline(self):
        self.assertEqual(minimum_Length("a\nb\nc"), 1)

    def test_string_with_tabs(self):
        self.assertEqual(minimum_Length("a\tb\nc"), 1)

    def test_string_with_carriage_return(self):
        self.assertEqual(minimum_Length("a\rnb\rc"), 1)
