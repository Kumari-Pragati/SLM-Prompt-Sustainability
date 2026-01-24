import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_vowels(""), "")

    def test_single_vowel(self):
        self.assertEqual(reverse_vowels("a"), "a")
        self.assertEqual(reverse_vowels("A"), "A")
        self.assertEqual(reverse_vowels("e"), "e")
        self.assertEqual(reverse_vowels("E"), "E")
        self.assertEqual(reverse_vowels("i"), "i")
        self.assertEqual(reverse_vowels("I"), "I")
        self.assertEqual(reverse_vowels("o"), "o")
        self.assertEqual(reverse_vowels("O"), "O")
        self.assertEqual(reverse_vowels("u"), "u")
        self.assertEqual(reverse_vowels("U"), "U")
        self.assertEqual(reverse_vowels("y"), "y")
        self.assertEqual(reverse_vowels("Y"), "Y")

    def test_single_consonant(self):
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

    def test_mixed_case(self):
        self.assertEqual(reverse_vowels("HeLLo"), "hElLo")
        self.assertEqual(reverse_vowels("hEllo"), "hElLo")
        self.assertEqual(reverse_vowels("HeLLoW"), "hElLoW")
        self.assertEqual(reverse_vowels("hElloW"), "hElLoW")
        self.assertEqual(reverse_vowels("HeLLO"), "hELLO")
        self.assertEqual(reverse_vowels("hELLO"), "hELLO")
        self.assertEqual(reverse_vowels("HeLlO"), "hElLo")
        self.assertEqual(reverse_vowels("hElLo"), "hElLo")

    def test_multiple_vowels(self):
        self.assertEqual(reverse_vowels("aeiou"), "uieoaE")
        self.assertEqual(reverse_vowels("AEIOU"), "UIOEa")
        self.assertEqual(reverse_vowels("AeIou"), "uioaE")
        self.assertEqual(reverse_vowels("aEiou"), "UioaE")
        self.assertEqual(reverse_vowels("AeIouY"), "uyioaE")
        self.assertEqual(reverse_vowels("aEiouY"), "UyioaE")
        self.assertEqual(reverse_vowels("AeIouX"), "uxioaE")
        self