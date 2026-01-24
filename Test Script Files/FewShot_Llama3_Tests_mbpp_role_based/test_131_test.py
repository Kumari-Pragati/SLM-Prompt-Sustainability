import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(reverse_vowels("hello"), "holle")

    def test_edge_case_empty_string(self):
        self.assertEqual(reverse_vowels(""), "")

    def test_edge_case_single_character(self):
        self.assertEqual(reverse_vowels("a"), "a")

    def test_edge_case_single_vowel(self):
        self.assertEqual(reverse_vowels("a"), "a")

    def test_edge_case_no_vowels(self):
        self.assertEqual(reverse_vowels("bcdfghjklmnpqrstvwxyz"), "bcdfghjklmnpqrstvwxyz")

    def test_edge_case_all_vowels(self):
        self.assertEqual(reverse_vowels("aeiouAEIOU"), "AEIOUaeiou")

    def test_edge_case_mixed_vowels(self):
        self.assertEqual(reverse_vowels("helloAEIOU"), "holleAEIOU")
