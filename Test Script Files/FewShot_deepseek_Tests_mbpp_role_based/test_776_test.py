import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_vowels('aeiou'), 0)
        self.assertEqual(count_vowels('aebec'), 1)
        self.assertEqual(count_vowels('aeiouaeiou'), 0)
        self.assertEqual(count_vowels('aeiouaeiouaeiou'), 1)

    def test_boundary_conditions(self):
        self.assertEqual(count_vowels(''), 0)
        self.assertEqual(count_vowels('a'), 1)
        self.assertEqual(count_vowels('eioua'), 1)
        self.assertEqual(count_vowels('aeiouaeiouaeiouaeiou'), 2)

    def test_edge_cases(self):
        self.assertEqual(count_vowels('bcdfg'), 0)
        self.assertEqual(count_vowels('aeioubcdfg'), 1)
        self.assertEqual(count_vowels('bcdfgaeiou'), 1)
        self.assertEqual(count_vowels('bcdfgaeioubcdfg'), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_vowels(123)
        with self.assertRaises(TypeError):
            count_vowels(['a', 'e', 'i', 'o', 'u'])
