import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):

    def test_unique_characters(self):
        self.assertTrue(unique_Characters("abcde"))
        self.assertFalse(unique_Characters("aabbcc"))
        self.assertTrue(unique_Characters("abcdefghijklmnopqrstuvwxyz"))
        self.assertFalse(unique_Characters("aabbccdd"))
        self.assertTrue(unique_Characters("1234567890"))
        self.assertFalse(unique_Characters("1234567890"))
        self.assertTrue(unique_Characters("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertFalse(unique_Characters("aabbccddEE"))
        self.assertTrue(unique_Characters("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertFalse(unique_Characters("aabbccddEE1234567890"))

    def test_empty_string(self):
        self.assertTrue(unique_Characters(""))

    def test_single_character(self):
        self.assertTrue(unique_Characters("a"))
        self.assertTrue(unique_Characters("1"))
        self.assertTrue(unique_Characters("A"))
        self.assertTrue(unique_Characters("0"))

    def test_no_characters(self):
        self.assertTrue(unique_Characters(""))
