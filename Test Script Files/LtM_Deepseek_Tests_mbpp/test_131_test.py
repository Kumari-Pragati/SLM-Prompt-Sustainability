import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(reverse_vowels("hello"), "holle")
        self.assertEqual(reverse_vowels("leetcode"), "leotcede")

    def test_edge_conditions(self):
        self.assertEqual(reverse_vowels(""), "")
        self.assertEqual(reverse_vowels("a"), "a")
        self.assertEqual(reverse_vowels("aeiou"), "uoiea")
        self.assertEqual(reverse_vowels("AEIOU"), "UOIEA")

    def test_complex_cases(self):
        self.assertEqual(reverse_vowels("AEIOUaeiou"), "UOIEAaeiou")
        self.assertEqual(reverse_vowels("The quick brown fox jumps over the lazy dog"),
                         "Thue kciuq wnrb ox jmu sps rovE thg lazy eod")
