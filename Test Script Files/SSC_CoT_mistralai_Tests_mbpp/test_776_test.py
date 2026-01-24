import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_vowels("hello"), 1)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("Hello"), 1)
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_vowels("a"), 1)
        self.assertEqual(count_vowels("aeiouy"), 5)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("aeiouaeiou"), 5)
        self.assertEqual(count_vowels("aeiouaeiouaeiou"), 6)
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiou"), 7)

    def test_special_cases(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiou"), 7)
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiou"), 8)
        self.assertEqual(count_vowels("aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou"), 9)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_vowels, 123)
        self.assertRaises(TypeError, count_vowels, [])
        self.assertRaises(TypeError, count_vowels, None)
