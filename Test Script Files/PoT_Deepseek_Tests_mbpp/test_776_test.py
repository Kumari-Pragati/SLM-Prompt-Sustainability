import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_vowels('aeiou'), 0)
        self.assertEqual(count_vowels('bcdfg'), 0)
        self.assertEqual(count_vowels('aeioubcdfg'), 0)
        self.assertEqual(count_vowels('aebucfg'), 1)
        self.assertEqual(count_vowels('aeiouaeiou'), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_vowels(''), 0)
        self.assertEqual(count_vowels('a'), 0)
        self.assertEqual(count_vowels('eioua'), 1)
        self.assertEqual(count_vowels('aeiouaeiouaeiou'), 0)

    def test_corner_cases(self):
        self.assertEqual(count_vowels('aeioub'), 1)
        self.assertEqual(count_vowels('bcdfgij'), 0)
        self.assertEqual(count_vowels('aeiouaeiouaeiouaeiou'), 0)
