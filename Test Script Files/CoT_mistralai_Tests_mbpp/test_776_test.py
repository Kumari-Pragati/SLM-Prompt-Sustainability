import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_vowels(''), 0)

    def test_single_vowel(self):
        self.assertEqual(count_vowels('a'), 1)
        self.assertEqual(count_vowels('e'), 1)
        self.assertEqual(count_vowels('i'), 1)
        self.assertEqual(count_vowels('o'), 1)
        self.assertEqual(count_vowels('u'), 1)

    def test_multiple_vowels(self):
        self.assertEqual(count_vowels('aeiou'), 1)
        self.assertEqual(count_vowels('AeIoU'), 1)
        self.assertEqual(count_vowels('Aeiou'), 1)
        self.assertEqual(count_vowels('aEiOu'), 1)

    def test_consecutive_vowels(self):
        self.assertEqual(count_vowels('aa'), 0)
        self.assertEqual(count_vowels('aei'), 1)
        self.assertEqual(count_vowels('ou'), 1)

    def test_vowel_at_start_and_end(self):
        self.assertEqual(count_vowels('aeiouaeiou'), 1)

    def test_non_vowel_at_start_and_end(self):
        self.assertEqual(count_vowels('xyzabcdefghijklmnopqrstuvwxyz'), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_vowels, 123)
        self.assertRaises(TypeError, count_vowels, [])
        self.assertRaises(TypeError, count_vowels, None)
        self.assertRaises(TypeError, count_vowels, ())
