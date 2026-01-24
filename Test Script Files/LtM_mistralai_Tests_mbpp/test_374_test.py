import unittest
from mbpp_374_code import permute_string

class TestPermuteString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(permute_string(''), [''])

    def test_single_character_string(self):
        self.assertEqual(permute_string('a'), ['a'])

    def test_two_character_string(self):
        self.assertEqual(permute_string('ab'), ['a', 'ba'])

    def test_three_character_string(self):
        self.assertEqual(permute_string('abc'), ['a', 'ac', 'ba', 'bc', 'ca', 'cb'])

    def test_longer_string(self):
        self.assertEqual(permute_string('abcdefg'), ['a', 'ac', 'ad', 'ae', 'af', 'ag', 'b', 'bc', 'bd', 'be', 'bf', 'bg', 'c', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'cg', 'd', 'da', 'db', 'dc', 'dd', 'de', 'df', 'dg', 'e', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'eg', 'f', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff', 'fg', 'g'])

    def test_duplicate_characters(self):
        self.assertEqual(permute_string('aa'), ['a', 'aa'])

    def test_all_same_characters(self):
        self.assertEqual(permute_string('aaaa'), ['a', 'aa', 'aaa', 'aaaa'])
