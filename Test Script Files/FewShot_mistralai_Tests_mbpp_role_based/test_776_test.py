import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_simple_string(self):
        self.assertEqual(count_vowels("hello"), 1)

    def test_string_with_multiple_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_string_with_only_vowels(self):
        self.assertEqual(count_vowels("Aeiou"), 5)

    def test_string_with_no_vowels(self):
        self.assertEqual(count_vowels("12345"), 0)

    def test_string_with_initial_vowel(self):
        self.assertEqual(count_vowels("A"), 0)
        self.assertEqual(count_vowels("E"), 1)
        self.assertEqual(count_vowels("I"), 1)
        self.assertEqual(count_vowels("O"), 1)
        self.assertEqual(count_vowels("U"), 1)

    def test_string_with_final_vowel(self):
        self.assertEqual(count_vowels("a"), 0)
        self.assertEqual(count_vowels("e"), 1)
        self.assertEqual(count_vowels("i"), 1)
        self.assertEqual(count_vowels("o"), 1)
        self.assertEqual(count_vowels("u"), 1)

    def test_string_with_initial_and_final_vowels(self):
        self.assertEqual(count_vowels("Aa"), 1)
        self.assertEqual(count_vowels("Ee"), 2)
        self.assertEqual(count_vowels("Ii"), 2)
        self.assertEqual(count_vowels("Oo"), 2)
        self.assertEqual(count_vowels("Uu"), 2)

    def test_string_with_multiple_consecutive_vowels(self):
        self.assertEqual(count_vowels("Ae"), 1)
        self.assertEqual(count_vowels("Ei"), 2)
        self.assertEqual(count_vowels("Io"), 2)
        self.assertEqual(count_vowels("Ou"), 2)
        self.assertEqual(count_vowels("Ua"), 1)
