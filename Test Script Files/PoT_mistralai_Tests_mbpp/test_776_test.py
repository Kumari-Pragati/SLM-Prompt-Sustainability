import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(count_vowels("hello"), 1)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("Hello"), 1)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("Aeiou"), 5)

    def test_edge_cases(self):
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("a"), 1)
        self.assertEqual(count_vowels("aeiouy"), 5)
        self.assertEqual(count_vowels("AEIOUY"), 5)
        self.assertEqual(count_vowels("AeIouY"), 5)

    def test_boundary_cases(self):
        self.assertEqual(count_vowels("a "), 1)
        self.assertEqual(count_vowels(" a "), 1)
        self.assertEqual(count_vowels(" ae "), 1)
        self.assertEqual(count_vowels(" ae "), 1)
        self.assertEqual(count_vowels(" ae\t"), 1)
        self.assertEqual(count_vowels(" ae\t"), 1)
