import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(unique_Characters('abcdefg'))

    def test_empty_string(self):
        self.assertTrue(unique_Characters(''))

    def test_single_character(self):
        self.assertTrue(unique_Characters('a'))

    def test_duplicate_characters(self):
        self.assertFalse(unique_Characters('aabbcc'))

    def test_case_sensitivity(self):
        self.assertTrue(unique_Characters('abcABC'))

    def test_whitespace(self):
        self.assertFalse(unique_Characters('a b c'))

    def test_special_characters(self):
        self.assertFalse(unique_Characters('a!b@c#'))
