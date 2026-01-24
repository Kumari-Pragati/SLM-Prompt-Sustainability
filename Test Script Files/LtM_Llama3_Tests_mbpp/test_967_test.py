import unittest
from mbpp_967_code import check

class TestCheckFunction(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(check("hello"), 'accepted')

    def test_simple_invalid_input(self):
        self.assertEqual(check("bcdfghjklmnpqrstvwxyz"), 'not accepted')

    def test_empty_input(self):
        self.assertEqual(check(""), 'not accepted')

    def test_single_vowel_input(self):
        self.assertEqual(check("a"), 'accepted')

    def test_multiple_vowels_input(self):
        self.assertEqual(check("aeiou"), 'accepted')

    def test_mixed_vowels_input(self):
        self.assertEqual(check("aeiouAEIOU"), 'accepted')

    def test_non_vowel_input(self):
        self.assertEqual(check("bcdfghjklmnpqrstvwxyz"), 'not accepted')

    def test_mixed_vowels_and_non_vowels_input(self):
        self.assertEqual(check("aeioubcdfghjklmnpqrstvwxyz"), 'accepted')
