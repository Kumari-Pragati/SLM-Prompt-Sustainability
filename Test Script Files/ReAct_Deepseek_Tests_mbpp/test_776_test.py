import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_vowels('hello'), 1)
        self.assertEqual(count_vowels('world'), 1)
        self.assertEqual(count_vowels('beautiful'), 2)
        self.assertEqual(count_vowels('beautifully'), 3)

    def test_edge_cases(self):
        self.assertEqual(count_vowels(''), 0)
        self.assertEqual(count_vowels('aeiou'), 0)
        self.assertEqual(count_vowels('a'), 0)
        self.assertEqual(count_vowels('e'), 0)
        self.assertEqual(count_vowels('i'), 0)
        self.assertEqual(count_vowels('o'), 0)
        self.assertEqual(count_vowels('u'), 0)

    def test_explicitly_handled_error_cases(self):
        self.assertEqual(count_vowels('123456'), 0)
        self.assertEqual(count_vowels('!@#$%^'), 0)
        self.assertEqual(count_vowels(' '), 0)
        self.assertEqual(count_vowels('aAeEiIoOuU'), 0)
