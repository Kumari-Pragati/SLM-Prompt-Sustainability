import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(unique_Characters(""))

    def test_single_character(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertTrue(unique_Characters(char))

    def test_duplicate_characters(self):
        self.assertFalse(unique_Characters("aa"))
        self.assertFalse(unique_Characters("abab"))
        self.assertFalse(unique_Characters("A1B2C3"))

    def test_mixed_case(self):
        self.assertTrue(unique_Characters("AaBbCc"))
        self.assertFalse(unique_Characters("AaAa"))

    def test_special_characters(self):
        self.assertTrue(unique_Characters("!@#$%^&*()_+-=[]{}|;:'\",.<>/? "))
        self.assertFalse(unique_Characters("!@#!@"))

    def test_numbers(self):
        self.assertTrue(unique_Characters("1234567890"))
        self.assertFalse(unique_Characters("121234"))

    def test_punctuation_and_numbers(self):
        self.assertTrue(unique_Characters("!@#$%^&*()_+-=[]{}|;:'\",.<>/? 1234567890"))
        self.assertFalse(unique_Characters("!@#!@12"))
