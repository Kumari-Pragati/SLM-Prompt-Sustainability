import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(reverse_vowels("hello"), "holle")

    def test_edge_case(self):
        self.assertEqual(reverse_vowels("aeiou"), "uoiea")

    def test_empty_string(self):
        self.assertEqual(reverse_vowels(""), "")

    def test_single_vowel(self):
        self.assertEqual(reverse_vowels("a"), "a")

    def test_no_vowels(self):
        self.assertEqual(reverse_vowels("bcdfghjklmnpqrstvwxyz"), "bcdfghjklmnpqrstvwxyz")

    def test_multiple_vowels(self):
        self.assertEqual(reverse_vowels("aeiouAEIOU"), "uoieaUOIEA")

    def test_mixed_case(self):
        self.assertEqual(reverse_vowels("HelloWorld"), "oellorH")

    def test_punctuation(self):
        self.assertEqual(reverse_vowels("Hello, World!"), "oellorW")

    def test_spaces(self):
        self.assertEqual(reverse_vowels("Hello World"), "oellorW")
