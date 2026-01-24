import unittest
from mbpp_374_code import permute_string

class TestPermuteString(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sorted(permute_string('abc')), sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))

    def test_empty_string(self):
        self.assertEqual(permute_string(''), [''])

    def test_single_character(self):
        self.assertEqual(permute_string('a'), ['a'])

    def test_duplicate_characters(self):
        self.assertEqual(sorted(permute_string('aa')), sorted(['aa', 'aa']))

    def test_long_string(self):
        self.assertEqual(sorted(permute_string('abcd')), sorted(['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
                                                                'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
                                                                'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
                                                                'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']))
