import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_vowels('aeiou'), 0)
        self.assertEqual(count_vowels('hello'), 1)
        self.assertEqual(count_vowels('beautiful'), 2)
        self.assertEqual(count_vowels('beautifully'), 3)

    def test_edge_cases(self):
        self.assertEqual(count_vowels(''), 0)
        self.assertEqual(count_vowels('a'), 0)
        self.assertEqual(count_vowels('e'), 0)
        self.assertEqual(count_vowels('i'), 0)
        self.assertEqual(count_vowels('o'), 0)
        self.assertEqual(count_vowels('u'), 0)

    def test_corner_cases(self):
        self.assertEqual(count_vowels('aeiouaeiou'), 0)
        self.assertEqual(count_vowels('aebecioud'), 2)
        self.assertEqual(count_vowels('aeiouaeiouaeiou'), 0)
        self.assertEqual(count_vowels('aeiouaeiouaeiouaeiou'), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_vowels(12345)
        with self.assertRaises(TypeError):
            count_vowels(['a', 'e', 'i', 'o', 'u'])
        with self.assertRaises(TypeError):
            count_vowels({'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5})
