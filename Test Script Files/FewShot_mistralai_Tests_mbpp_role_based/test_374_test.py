import unittest
from mbpp_374_code import permute_string

class TestPermuteString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(permute_string(''), [''])

    def test_single_character_string(self):
        self.assertEqual(permute_string('a'), ['a'])

    def test_two_character_string(self):
        self.assertEqual(permute_string('ab'), ['a', 'ba'])

    def test_longer_string(self):
        self.assertEqual(permute_string('abc'), ['a', 'ac', 'ba', 'bc', 'ca', 'cb'])

    def test_duplicate_characters(self):
        self.assertEqual(permute_string('aa'), ['a', 'aa'])

    def test_multiple_duplicate_characters(self):
        self.assertEqual(permute_string('aaa'), ['a', 'aa', 'aaa'])

    def test_long_string_with_duplicates(self):
        self.assertEqual(permute_string('aaaaab'), ['a', 'aa', 'aaa', 'aaab', 'aaaba', 'aab', 'aaba', 'ab', 'ba'])
