import unittest
from mbpp_374_code import permute_string

class TestPermuteString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(permute_string(''), [''])

    def test_single_character_string(self):
        self.assertEqual(permute_string('a'), ['a'])

    def test_two_character_string(self):
        self.assertEqual(sorted(permute_string('ab')), ['ab', 'ba'])

    def test_three_character_string(self):
        self.assertEqual(sorted(permute_string('abc')), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test_duplicate_characters(self):
        self.assertEqual(sorted(permute_string('aa')), ['aa'])

    def test_large_string(self):
        self.assertEqual(len(permute_string('abcd')), 24)

    def test_special_characters(self):
        self.assertEqual(sorted(permute_string('!@#')), ['!@#', '@!#', '@#!', '#!@', '#@!', '!#@'])
