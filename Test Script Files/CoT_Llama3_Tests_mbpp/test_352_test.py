import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):

    def test_unique_characters(self):
        self.assertTrue(unique_Characters("abcde"))
    def test_non_unique_characters(self):
        self.assertFalse(unique_Characters("aabbcc"))
    def test_empty_string(self):
        self.assertTrue(unique_Characters(""))

    def test_single_character(self):
        self.assertTrue(unique_Characters("a"))

    def test_all_same_characters(self):
        self.assertFalse(unique_Characters("aaaaaa"))

    def test_no_characters(self):
        self.assertTrue(unique_Characters(""))
