import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_vowels('aeiou'), 0)
        self.assertEqual(count_vowels('aebec'), 1)
        self.assertEqual(count_vowels('aeiouaeiou'), 0)
        self.assertEqual(count_vowels('aeiouaeiouaeiou'), 1)

    def test_edge_cases(self):
        self.assertEqual(count_vowels(''), 0)
        self.assertEqual(count_vowels('b'), 0)
        self.assertEqual(count_vowels('ab'), 1)
        self.assertEqual(count_vowels('ba'), 1)
        self.assertEqual(count_vowels('aab'), 1)
        self.assertEqual(count_vowels('baa'), 1)

    def test_boundary_conditions(self):
        self.assertEqual(count_vowels('a'), 1)
        self.assertEqual(count_vowels('b'), 0)
        self.assertEqual(count_vowels('ab'), 1)
        self.assertEqual(count_vowels('ba'), 1)
        self.assertEqual(count_vowels('abc'), 1)
        self.assertEqual(count_vowels('bca'), 1)
        self.assertEqual(count_vowels('cab'), 1)
        self.assertEqual(count_vowels('cba'), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_vowels(123)
        with self.assertRaises(TypeError):
            count_vowels(['a', 'b', 'c'])
        with self.assertRaises(TypeError):
            count_vowels({'a': 1, 'b': 2, 'c': 3})
