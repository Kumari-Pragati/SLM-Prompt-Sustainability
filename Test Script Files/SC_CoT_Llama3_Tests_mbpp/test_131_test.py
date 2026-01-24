import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(reverse_vowels("hello"), "holle")

    def test_edge_case_empty_string(self):
        self.assertEqual(reverse_vowels(""), "")

    def test_edge_case_single_vowel(self):
        self.assertEqual(reverse_vowels("a"), "a")

    def test_edge_case_single_non_vowel(self):
        self.assertEqual(reverse_vowels("b"), "b")

    def test_edge_case_all_vowels(self):
        self.assertEqual(reverse_vowels("aeiou"), "uoiea")

    def test_edge_case_all_non_vowels(self):
        self.assertEqual(reverse_vowels("bcdfghjklmnpqrstvwxyz"), "vwxyzjklmnpqrstbcdfgh")

    def test_edge_case_mixed_vowels_and_non_vowels(self):
        self.assertEqual(reverse_vowels("hello world"), "holle dlrow")

    def test_edge_case_mixed_case(self):
        self.assertEqual(reverse_vowels("Hello World"), "Holle dlroW")

    def test_edge_case_punctuation(self):
        self.assertEqual(reverse_vowels("Hello, World!"), "Holle, dlroW!")

    def test_edge_case_numbers(self):
        self.assertEqual(reverse_vowels("Hello123 World!"), "Holle 321 dlroW!")

    def test_edge_case_special_characters(self):
        self.assertEqual(reverse_vowels("Hello@World!"), "Holle @ dlroW!")
