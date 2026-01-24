import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_vowels('aeiou'), 0)
        self.assertEqual(count_vowels('aebec'), 1)
        self.assertEqual(count_vowels('aeiouaeiou'), 0)
        self.assertEqual(count_vowels('aeiouaeiouaeiou'), 0)

    def test_edge_conditions(self):
        self.assertEqual(count_vowels(''), 0)
        self.assertEqual(count_vowels('a'), 0)
        self.assertEqual(count_vowels('ae'), 0)
        self.assertEqual(count_vowels('aei'), 0)
        self.assertEqual(count_vowels('aeio'), 0)
        self.assertEqual(count_vowels('aeiou'), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count_vowels('a' * 10000), 0)
        self.assertEqual(count_vowels('b' * 10000), 10000)

    def test_complex_cases(self):
        self.assertEqual(count_vowels('bbaeioubba'), 2)
        self.assertEqual(count_vowels('aeioubbaeiou'), 2)
        self.assertEqual(count_vowels('aeioubbaeioubba'), 2)
        self.assertEqual(count_vowels('bbaeioubbaeiou'), 4)
