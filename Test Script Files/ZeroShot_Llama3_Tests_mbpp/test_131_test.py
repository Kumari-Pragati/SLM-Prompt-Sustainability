import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):

    def test_reverse_vowels(self):
        self.assertEqual(reverse_vowels("hello"), "holle")
        self.assertEqual(reverse_vowels("AaEoOo"), "oOoEaA")
        self.assertEqual(reverse_vowels("aeiou"), "uoiea")
        self.assertEqual(reverse_vowels("AEIOU"), "UOIEA")
        self.assertEqual(reverse_vowels("a"), "a")
        self.assertEqual(reverse_vowels("AEIOU"), "UOIEA")
        self.assertEqual(reverse_vowels("hello world"), "holle dlrow")
        self.assertEqual(reverse_vowels("AEIOUAEIOU"), "UOIEAUOIEA")
        self.assertEqual(reverse_vowels("aAeEoOo"), "oOoEaA")
        self.assertEqual(reverse_vowels("AEIOUAEIOU"), "UOIEAUOIEA")

    def test_reverse_vowels_empty_string(self):
        self.assertEqual(reverse_vowels(""), "")

    def test_reverse_vowels_single_char(self):
        self.assertEqual(reverse_vowels("a"), "a")
        self.assertEqual(reverse_vowels("A"), "A")
