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

    def test_multiple_vowels(self):
        self.assertEqual(reverse_vowels("aeiou"), "uieoa")
        self.assertEqual(reverse_vowels("AEIOU"), "UIOAE")
        self.assertEqual(reverse_vowels("AeIoU"), "UoIEA")
        self.assertEqual(reverse_vowels("aEiOu"), "uOiea")
        self.assertEqual(reverse_vowels("AeIoU"), "UoIeA")
        self.assertEqual(reverse_vowels("aEiOu!"), "uOieA!")
        self.assertEqual(reverse_vowels("AeIou!"), "UoIeA!")

    def test_mixed_case(self):
        self.assertEqual(reverse_vowels("HeLLo"), "olleH")
        self.assertEqual(reverse_vowels("hELlo"), "olleh")
        self.assertEqual(reverse_vowels("HeLlO"), "olleH")
        self.assertEqual(reverse_vowels("HeLlO!"), "olleH!")
        self.assertEqual(reverse_vowels("hElLo"), "olleh")
        self.assertEqual(reverse_vowels("hElLo"), "olleh")
        self.assertEqual(reverse_vowels("hEllO"), "olleH")
        self.assertEqual(reverse_vowels("hEllO!"), "olleH!")

    def test_punctuation(self):
        self.assertEqual(reverse_vowels("He,LlO!"), "olleH!,")
        self.assertEqual(reverse_vowels("He,LlO."), "olleH.,")
        self.assertEqual(reverse_vowels("He,LlO."), "olleH.,")
        self.assertEqual(reverse_vowels("He,LlO,!"), "olleH,!")
        self.assertEqual(reverse_vowels("He,LlO,!"), "olleH,!")
        self.assertEqual(reverse_vowels("He,LlO,!"), "olleH,!")
        self.assertEqual(reverse_vowels("He,LlO,!"), "olleH,!")

    def test_special_characters(self):
        self.assertEqual(reverse_vowels("He_LlO#!"), "olleH#!")
        self.assertEqual(reverse_vowels("He_LlO#@"), "olleH#@")
        self.assertEqual(reverse_vowels("He_LlO#@$"), "olleH#@$")
        self.assertEqual(reverse_vowels("He_LlO#@$%"), "olleH#@$%")
        self.assertEqual(reverse_vowels("He_LlO#@$%^"), "olleH#@$%^")
