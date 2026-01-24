import unittest
from mbpp_374_code import permute_string

class TestPermuteString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(permute_string(''), [''])

    def test_single_character_string(self):
        self.assertEqual(permute_string('a'), ['a'])

    def test_two_character_string(self):
        self.assertEqual(permute_string('ab'), ['ab', 'ba'])

    def test_three_character_string(self):
        self.assertEqual(permute_string('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test_four_character_string(self):
        self.assertEqual(permute_string('abcd'), ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 
                                                  'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 
                                                  'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 
                                                  'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'])
