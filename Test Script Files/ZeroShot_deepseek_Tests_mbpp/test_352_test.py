import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):

    def test_unique_characters(self):
        self.assertTrue(unique_Characters('abcde'))
        self.assertFalse(unique_Characters('aabcde'))
        self.assertFalse(unique_Characters('aabbcde'))
        self.assertFalse(unique_Characters('aabbccde'))
        self.assertFalse(unique_Characters('aabbccdde'))
        self.assertTrue(unique_Characters(''))
        self.assertTrue(unique_Characters('a'))
        self.assertFalse(unique_Characters('aa'))
