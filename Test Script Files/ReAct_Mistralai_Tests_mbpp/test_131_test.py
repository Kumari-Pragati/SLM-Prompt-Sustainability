import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_vowels(""), "")

    def test_single_vowel(self):
        for vowel in "aeiouAEIOU":
            self.assertEqual(reverse_vowels(vowel), vowel[::-1])

    def test_single_consonant(self):
        for consonant in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ1234567890!@#$%^&*()_+-=[]{};':\"|,.<>/? ":
            self.assertEqual(reverse_vowels(consonant), consonant)

    def test_mixed_case(self):
        test_strings = [
            "Hello, World!",
            "A-E-I-O-U",
            "1234567890",
            "!@#$%^&*()_+-=[]{};':\"|,.<>/? ",
            "HeLLo, wOrLd!",
            "HeLlO, wOrLd!",
            "HeLlO, WoRlD!",
            "HeLlO, wOrLd!",
            "HeLlO, wOrLd!",
            "HeLlO, wOrLd!",
        ]
        for test_string in test_strings:
            self.assertEqual(reverse_vowels(test_string), test_string[::-1])

    def test_multiple_vowels(self):
        test_strings = [
            "aeiou",
            "AeIou",
            "AeIouX",
            "AeIou123",
            "AeIou!@#$%^&*()_+-=[]{};':\"|,.<>/? ",
        ]
        for test_string in test_strings:
            self.assertEqual(reverse_vowels(test_string), test_string[::-1])

    def test_long_string(self):
        test_string = "aeiouabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{};':\"|,.<>/? " * 100
        self.assertEqual(reverse_vowels(test_string), test_string[::-1])
