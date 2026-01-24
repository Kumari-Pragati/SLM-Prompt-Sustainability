import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(reverse_vowels("hello"), "holle")
        self.assertEqual(reverse_vowels("aeiou"), "uoiea")
        self.assertEqual(reverse_vowels("AEIOU"), "UOIEA")
        self.assertEqual(reverse_vowels("a"), "a")
        self.assertEqual(reverse_vowels("AE"), "EA")

    def test_edge(self):
        self.assertEqual(reverse_vowels(""), "")
        self.assertEqual(reverse_vowels("a"), "a")
        self.assertEqual(reverse_vowels("AEIOU"), "UOIEA")
        self.assertEqual(reverse_vowels("aeiou"), "uoiea")

    def test_complex(self):
        self.assertEqual(reverse_vowels("hello world"), "holle dlrow")
        self.assertEqual(reverse_vowels("AEIOUaeiou"), "UOIEAuoiea")
        self.assertEqual(reverse_vowels("AEIOUAEIOU"), "UOIEAUOIEA")
