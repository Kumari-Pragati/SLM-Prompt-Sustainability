import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_vowels(''), 0)

    def test_single_vowel(self):
        for vowel in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            self.assertEqual(count_vowels(vowel), 1)

    def test_multiple_vowels(self):
        test_str = 'aeiou'
        self.assertEqual(count_vowels(test_str), len(test_str))

    def test_consecutive_vowels(self):
        test_str = 'aeiou'
        self.assertEqual(count_vowels(test_str), 1)

    def test_consecutive_non_vowels(self):
        test_str = 'xyz'
        self.assertEqual(count_vowels(test_str), 0)

    def test_vowel_before_non_vowel(self):
        test_str = 'aez'
        self.assertEqual(count_vowels(test_str), 1)

    def test_non_vowel_before_vowel(self):
        test_str = 'zya'
        self.assertEqual(count_vowels(test_str), 1)

    def test_vowel_before_and_after_non_vowel(self):
        test_str = 'azy'
        self.assertEqual(count_vowels(test_str), 0)

    def test_boundary_cases(self):
        test_str = 'a'
        self.assertEqual(count_vowels(test_str), 1)
        test_str = 'aeiou' + 'a'
        self.assertEqual(count_vowels(test_str), 5)
        test_str = 'aeiou' + ' '
        self.assertEqual(count_vowels(test_str), 5)
        test_str = ' ' + 'aeiou'
        self.assertEqual(count_vowels(test_str), 5)
        test_str = ' '
        self.assertEqual(count_vowels(test_str), 0)
