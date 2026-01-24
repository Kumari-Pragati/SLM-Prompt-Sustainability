import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):

    def test_unique_characters_normal(self):
        self.assertTrue(unique_Characters("abcdefg"))
        self.assertTrue(unique_Characters("1234567"))
        self.assertTrue(unique_Characters("ABCDEFG"))
        self.assertTrue(unique_Characters("!@#$%^&*"))

    def test_unique_characters_edge_cases(self):
        self.assertFalse(unique_Characters("aab"))
        self.assertFalse(unique_Characters("aaa"))
        self.assertFalse(unique_Characters("111"))
        self.assertFalse(unique_Characters("ABAB"))
        self.assertFalse(unique_Characters("!@!@"))
        self.assertFalse(unique_Characters("AABC"))
        self.assertFalse(unique_Characters("12345"))

    def test_unique_characters_empty_string(self):
        self.assertTrue(unique_Characters(""))

    def test_unique_characters_single_char(self):
        self.assertTrue(unique_Characters("a"))
        self.assertTrue(unique_Characters("1"))
        self.assertTrue(unique_Characters("A"))
        self.assertTrue(unique_Characters("!"))
