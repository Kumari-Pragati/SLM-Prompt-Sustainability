import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("world"), 1)
        self.assertEqual(count_vowels("python"), 2)

    def test_edge(self):
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("a"), 0)
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_boundary(self):
        self.assertEqual(count_vowels("a"), 0)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("hello world"), 3)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            count_vowels(None)
        with self.assertRaises(TypeError):
            count_vowels(123)
