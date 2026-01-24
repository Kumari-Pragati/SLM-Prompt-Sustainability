import unittest
from mbpp_667_code import Check_Vow

class TestCheckVow(unittest.TestCase):
    def test_valid_string_with_vowels(self):
        self.assertEqual(Check_Vow("Hello", "aeiou"), 2)

    def test_valid_string_with_no_vowels(self):
        self.assertEqual(Check_Vow("Goodbye", "aeiou"), 0)

    def test_string_with_only_vowels(self):
        self.assertEqual(Check_Vow("AeioU", "aeiou"), 5)

    def test_string_with_repeated_vowels(self):
        self.assertEqual(Check_Vow("AaaaEeee", "aeiou"), 5)

    def test_empty_string(self):
        self.assertEqual(Check_Vow("", "aeiou"), 0)

    def test_string_with_only_non_vowels(self):
        self.assertEqual(Check_Vow("12345", "aeiou"), 0)

    def test_string_with_special_characters(self):
        self.assertEqual(Check_Vow("!@#$%^&*()_+-=", "aeiou"), 0)

    def test_string_with_numbers(self):
        self.assertEqual(Check_Vow("12345", "aeiou"), 0)

    def test_string_with_whitespace(self):
        self.assertEqual(Check_Vow(" Hello ", "aeiou"), 0)

    def test_string_with_uppercase_vowels(self):
        self.assertEqual(Check_Vow("HELLO", "aeiou"), 1)
