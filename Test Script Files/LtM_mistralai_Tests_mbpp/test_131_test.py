import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(reverse_vowels("hello"), "holle")

    def test_case_with_uppercase_vowels(self):
        self.assertEqual(reverse_vowels("HELLO"), "hOLLE")

    def test_case_with_only_vowels(self):
        self.assertEqual(reverse_vowels("aeiou"), "ouaei")

    def test_case_with_only_consonants(self):
        self.assertEqual(reverse_vowels("tcsr"), "rsc")

    def test_case_with_initial_and_final_vowels(self):
        self.assertEqual(reverse_vowels("aeiouaei"), "ieouaea")

    def test_case_with_multiple_consecutive_vowels(self):
        self.assertEqual(reverse_vowels("aeiouaeiou"), "ouieouaeia")

    def test_case_with_vowels_in_middle(self):
        self.assertEqual(reverse_vowels("aeioubcdfghjeiou"), "ouieoubdfghjceai")

    def test_empty_string(self):
        self.assertEqual(reverse_vowels(""), "")

    def test_single_vowel(self):
        self.assertEqual(reverse_vowels("a"), "a")
