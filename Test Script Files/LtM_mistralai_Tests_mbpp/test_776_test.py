import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_simple_vowel_string(self):
        self.assertEqual(count_vowels("aeiou"), 0)
        self.assertEqual(count_vowels("Aeiou"), 0)
        self.assertEqual(count_vowels("aAeIoU"), 3)

    def test_edge_cases(self):
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("a"), 1)
        self.assertEqual(count_vowels("aeiouAEIOU"), 8)
        self.assertEqual(count_vowels("aeiouAEIOU "), 8)
        self.assertEqual(count_vowels("aeiouAEIOU\t"), 8)
        self.assertEqual(count_vowels("aeiouAEIOU\n"), 8)

    def test_boundary_conditions(self):
        self.assertEqual(count_vowels("aA"), 1)
        self.assertEqual(count_vowels("Aa"), 1)
        self.assertEqual(count_vowels("aAe"), 1)
        self.assertEqual(count_vowels("AaE"), 1)
        self.assertEqual(count_vowels("aeiouAEIOUaeiou"), 12)
        self.assertEqual(count_vowels("aeiouAEIOUaeiou "), 12)
        self.assertEqual(count_vowels("aeiouAEIOUaeiou\t"), 12)
        self.assertEqual(count_vowels("aeiouAEIOUaeiou\n"), 12)

    def test_complex_cases(self):
        self.assertEqual(count_vowels("aAeIoUaA"), 3)
        self.assertEqual(count_vowels("aeiouAEIOUaeiouAEIOU"), 12)
        self.assertEqual(count_vowels("aeiouAEIOUaeiouAEIOUaeiou"), 12)
        self.assertEqual(count_vowels("aeiouAEIOUaeiouAEIOUaeiouAEIOU"), 12)
