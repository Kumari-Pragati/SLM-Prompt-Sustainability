import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):

    def test_reverse_vowels(self):
        self.assertEqual(reverse_vowels("hello"), "holle")
        self.assertEqual(reverse_vowels("Leetcode"), "Leotcede")
        self.assertEqual(reverse_vowels("AEIOU"), "UOIEA")
        self.assertEqual(reverse_vowels("aeiou"), "uoiea")
        self.assertEqual(reverse_vowels(""), "")
        self.assertEqual(reverse_vowels("bcdfghjklmnpqrstvwxyz"), "bcdfghjklmnpqrstvwxyz")
        self.assertEqual(reverse_vowels("AEIOUaeiou"), "uoieaUOIEA")
