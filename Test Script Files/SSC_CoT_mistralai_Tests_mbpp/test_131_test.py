import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(reverse_vowels("hello"), "holle")
        self.assertEqual(reverse_vowels("Hello"), "hOllo")
        self.assertEqual(reverse_vowels("leetcode"), "leetcedoC")

    def test_edge_cases(self):
        self.assertEqual(reverse_vowels(""), "")
        self.assertEqual(reverse_vowels("a"), "a")
        self.assertEqual(reverse_vowels("aeiou"), "ouiea")
        self.assertEqual(reverse_vowels("AEIOU"), "UIOEA")

    def test_boundary_cases(self):
        self.assertEqual(reverse_vowels("aeiouAEIOU"), "UEIOUAeiou")
        self.assertEqual(reverse_vowels("AEIOUaeiou"), "aeiouUEIOU")

    def test_special_cases(self):
        self.assertEqual(reverse_vowels("heLLo"), "heolL")
        self.assertEqual(reverse_vowels("HeLLo"), "HeolL")
        self.assertEqual(reverse_vowels("heLLO"), "heOLLO")
        self.assertEqual(reverse_vowels("HeLLO"), "HeOLLO")
