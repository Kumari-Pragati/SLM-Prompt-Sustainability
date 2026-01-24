import unittest
from mbpp_667_code import Check_Vow

class TestCheckVow(unittest.TestCase):

    def test_simple_vowels(self):
        self.assertEqual(Check_Vow("hello", "aeiou"), 2)
        self.assertEqual(Check_Vow("Hello", "AEIOU"), 2)

    def test_single_vowel(self):
        self.assertEqual(Check_Vow("a", "aeiou"), 1)
        self.assertEqual(Check_Vow("A", "AEIOU"), 1)

    def test_empty_string(self):
        self.assertEqual(Check_Vow("", "aeiou"), 0)

    def test_no_vowels(self):
        self.assertEqual(Check_Vow("spam", "aeiou"), 0)

    def test_mixed_case(self):
        self.assertEqual(Check_Vow("HeLlO wOrLd", "aeiou"), 3)

    def test_special_characters(self):
        self.assertEqual(Check_Vow("!@#$%^&*()_+-=", "aeiou"), 0)

    def test_vowels_with_digits(self):
        self.assertEqual(Check_Vow("hello123", "aeiou"), 2)
