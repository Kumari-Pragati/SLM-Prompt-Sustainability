import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(reverse_vowels("hello"), "holle")
        self.assertEqual(reverse_vowels("leetcode"), "letcode")
        self.assertEqual(reverse_vowels("A man, a plan, a canal: Panama"), "A man, a plan, a canal: Namapak")

    def test_edge_case_empty_string(self):
        self.assertEqual(reverse_vowels(""), "")

    def test_edge_case_single_vowel(self):
        self.assertEqual(reverse_vowels("a"), "a")
        self.assertEqual(reverse_vowels("e"), "e")
        self.assertEqual(reverse_vowels("o"), "o")
        self.assertEqual(reverse_vowels("u"), "u")
        self.assertEqual(reverse_vowels("i"), "i")
        self.assertEqual(reverse_vowels("y"), "y")

    def test_edge_case_single_consonant(self):
        self.assertEqual(reverse_vowels("b"), "b")
        self.assertEqual(reverse_vowels("c"), "c")
        self.assertEqual(reverse_vowels("d"), "d")
        self.assertEqual(reverse_vowels("f"), "f")
        self.assertEqual(reverse_vowels("g"), "g")
        self.assertEqual(reverse_vowels("h"), "h")
        self.assertEqual(reverse_vowels("j"), "j")
        self.assertEqual(reverse_vowels("k"), "k")
        self.assertEqual(reverse_vowels("l"), "l")
        self.assertEqual(reverse_vowels("m"), "m")
        self.assertEqual(reverse_vowels("n"), "n")
        self.assertEqual(reverse_vowels("p"), "p")
        self.assertEqual(reverse_vowels("q"), "q")
        self.assertEqual(reverse_vowels("r"), "r")
        self.assertEqual(reverse_vowels("s"), "s")
        self.assertEqual(reverse_vowels("t"), "t")
        self.assertEqual(reverse_vowels("v"), "v")
        self.assertEqual(reverse_vowels("w"), "w")
        self.assertEqual(reverse_vowels("x"), "x")
        self.assertEqual(reverse_vowels("z"), "z")

    def test_edge_case_mixed_vowels_consonants(self):
        self.assertEqual(reverse_vowels("aeiou"), "ouiea")
        self.assertEqual(reverse_vowels("abcdefghijklmnopqrstuvwxyz"), "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(reverse_vowels("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
