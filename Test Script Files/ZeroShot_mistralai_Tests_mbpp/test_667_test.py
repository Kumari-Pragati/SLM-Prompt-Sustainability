import unittest
from mbpp_667_code import Check_Vow

class TestCheckVow(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(Check_Vow("", set("aeiou")), 0)

    def test_string_with_vowels(self):
        self.assertEqual(Check_Vow("hello", set("aeiou")), 3)

    def test_string_with_no_vowels(self):
        self.assertEqual(Check_Vow("spam", set("aeiou")), 0)

    def test_string_with_repeated_vowels(self):
        self.assertEqual(Check_Vow("aaaeee", set("aeiou")), 5)

    def test_string_with_non_vowel_characters(self):
        self.assertEqual(Check_Vow("12345", set("aeiou")), 0)

    def test_string_with_vowels_and_non_vowels(self):
        self.assertEqual(Check_Vow("hey123", set("aeiou")), 2)
