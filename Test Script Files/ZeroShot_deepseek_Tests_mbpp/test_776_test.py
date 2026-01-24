import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowels('aeiou'), 0)
        self.assertEqual(count_vowels('aebec'), 1)
        self.assertEqual(count_vowels('aeiouaeiou'), 0)
        self.assertEqual(count_vowels('aeiouaeiouaeiou'), 1)
        self.assertEqual(count_vowels('bcdfg'), 0)
        self.assertEqual(count_vowels('aeioubcdfg'), 1)
        self.assertEqual(count_vowels('aeioubcdfgaeiou'), 2)
        self.assertEqual(count_vowels('aeioubcdfgaeiouaeiou'), 3)
        self.assertEqual(count_vowels(''), 0)
        self.assertEqual(count_vowels('a'), 1)
        self.assertEqual(count_vowels('eioua'), 1)
        self.assertEqual(count_vowels('ouiea'), 1)
