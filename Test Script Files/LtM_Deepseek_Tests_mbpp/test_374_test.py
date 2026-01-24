import unittest
from mbpp_374_code import permute_string

class TestPermuteString(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(permute_string('ab'), sorted(['ba', 'ab']))

    def test_empty_input(self):
        self.assertEqual(permute_string(''), [''])

    def test_single_character_input(self):
        self.assertEqual(permute_string('a'), ['a'])

    def test_duplicate_characters(self):
        self.assertEqual(sorted(permute_string('aa')), sorted(['aa', 'aa']))

    def test_multiple_characters(self):
        self.assertEqual(sorted(permute_string('abc')), sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))

    def test_long_string(self):
        self.assertEqual(sorted(permute_string('abcd')), sorted(['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
                                                                 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
                                                                 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
                                                                 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']))
