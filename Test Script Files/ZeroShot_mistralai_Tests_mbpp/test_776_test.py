import unittest
from776_code import count_vowels

class TestCountVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_single_vowel(self):
        self.assertEqual(count_vowels("a"), 1)
        self.assertEqual(count_vowels("e"), 1)
        self.assertEqual(count_vowels("i"), 1)
        self.assertEqual(count_vowels("o"), 1)
        self.assertEqual(count_vowels("u"), 1)

    def test_multiple_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AeIoU"), 5)
        self.assertEqual(count_vowels("aEiOu"), 5)

    def test_vowel_at_start_and_end(self):
        self.assertEqual(count_vowels("aa"), 1)
        self.assertEqual(count_vowels("oo"), 1)
        self.assertEqual(count_vowels("ee"), 1)
        self.assertEqual(count_vowels("ii"), 1)
        self.assertEqual(count_vowels("uu"), 1)

    def test_vowel_at_start_and_not_at_end(self):
        self.assertEqual(count_vowels("ae"), 1)
        self.assertEqual(count_vowels("ei"), 1)
        self.assertEqual(count_vowels("ou"), 1)
        self.assertEqual(count_vowels("iu"), 1)
        self.assertEqual(count_vowels("au"), 0)

    def test_not_vowel_at_start_and_end(self):
        self.assertEqual(count_vowels("xyz"), 0)
        self.assertEqual(count_vowels("123"), 0)
        self.assertEqual(count_vowels("!@#"), 0)

    def test_consecutive_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 4)
        self.assertEqual(count_vowels("AeIoU"), 4)
        self.assertEqual(count_vowels("aEiOu"), 4)

    def test_consecutive_non_vowels(self):
        self.assertEqual(count_vowels("xyz"), 0)
        self.assertEqual(count_vowels("123"), 0)
        self.assertEqual(count_vowels("!@#"), 0)

    def test_mixed_case(self):
        self.assertEqual(count_vowels("AeIoU"), 4)
        self.assertEqual(count_vowels("aEiOu"), 4)
