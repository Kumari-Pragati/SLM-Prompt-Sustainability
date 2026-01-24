import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(reverse_vowels("hello"), "holle")

    def test_all_vowels(self):
        self.assertEqual(reverse_vowels("aeiou"), "uoiea")

    def test_no_vowels(self):
        self.assertEqual(reverse_vowels("bcdfghjklmnpqrstvwxyz"), "bcdfghjklmnpqrstvwxyz")

    def test_empty_string(self):
        self.assertEqual(reverse_vowels(""), "")

    def test_mixed_case(self):
        self.assertEqual(reverse_vowels("HeLlO"), "HeLlO")

    def test_special_characters(self):
        self.assertEqual(reverse_vowels("hel!lo"), "hel!lo")

    def test_numbers(self):
        self.assertEqual(reverse_vowels("h3ll0"), "h3ll0")
