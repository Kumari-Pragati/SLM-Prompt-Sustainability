import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):

    def test_simple_single_char(self):
        self.assertEqual(first_non_repeating_character("a"), "a")

    def test_simple_multiple_chars(self):
        self.assertEqual(first_non_repeating_character("abc"), "a")

    def test_simple_repeated_chars(self):
        self.assertEqual(first_non_repeating_character("aa"), None)

    def test_edge_single_char_repeat(self):
        self.assertEqual(first_non_repeating_character("aaa"), None)

    def test_edge_multiple_chars_repeat(self):
        self.assertEqual(first_non_repeating_character("aaabbc"), "b")

    def test_edge_empty_string(self):
        self.assertEqual(first_non_repeating_character(""), None)

    def test_edge_single_digit(self):
        self.assertEqual(first_non_repeating_character("123"), None)

    def test_edge_special_chars(self):
        self.assertEqual(first_non_repeating_character("!@#$%^&*()"), None)

    def test_complex_multiple_repeated_chars(self):
        self.assertEqual(first_non_repeating_character("aabbaabba"), "a")
