import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(reverse_vowels('hello'), 'holle')

    def test_edge_case(self):
        self.assertEqual(reverse_vowels('a'), 'a')

    def test_boundary_case(self):
        self.assertEqual(reverse_vowels('aeiou'), 'uoiea')

    def test_special_case(self):
        self.assertEqual(reverse_vowels('AEIOU'), 'UOIEA')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            reverse_vowels(123)
