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
        self.assertEqual(reverse_vowels("aeiou"), "ouaei")
        self.assertEqual(reverse_vowels("AEIOU"), "UIOAE")
        self.assertEqual(reverse_vowels("Hello"), "hOllo" )
        self.assertEqual(reverse_vowels("hello"), "hElLo" )
        self.assertEqual(reverse_vowels("HeLLo"), "hOlle" )
        self.assertEqual(reverse_vowels("HELLO"), "hOLLO" )

    def test_mixed_case_and_punctuation(self):
        self.assertEqual(reverse_vowels("!Ae!I@oU"), "!uO!iA@eO" )
        self.assertEqual(reverse_vowels("!Ae!I@oU, !aE!i@oU."), "!uO, !oU!iA@e!Ae!I." )
        self.assertEqual(reverse_vowels("!Ae!I@oU, !aE!i@oU.".upper()), "!UO, !OU!IA@EO!AE!I." )

    def test_invalid_input(self):
        self.assertRaises(TypeError, reverse_vowels, 123)
        self.assertRaises(TypeError, reverse_vowels, None)
        self.assertRaises(TypeError, reverse_vowels, [])
