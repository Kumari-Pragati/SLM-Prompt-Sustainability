import unittest
from mbpp_374_code import permute_string

class TestPermuteString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(permute_string(''), [''])

    def test_single_character_string(self):
        self.assertEqual(permute_string('a'), ['a'])

    def test_two_character_string(self):
        self.assertEqual(permute_string('ab'), ['ba', 'ab'])

    def test_three_character_string(self):
        self.assertEqual(permute_string('abc'), ['acb', 'bac', 'bca', 'cab'])

    def test_four_character_string(self):
        self.assertEqual(permute_string('abcd'), ['acbd', 'adbc', 'bacd', 'badc', 'bcad', 'cbad', 'cbad', 'dabc', 'dbac'])

    def test_string_with_repeated_characters(self):
        self.assertEqual(permute_string('aaab'), ['aabaa', 'aaaba', 'aaabba', 'abaaa', 'aaba', 'aabba', 'baaab', 'baba'])
