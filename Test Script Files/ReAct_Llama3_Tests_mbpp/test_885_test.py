import unittest
from mbpp_885_code import is_Isomorphic

class TestIsIsomorphic(unittest.TestCase):

    def test_isomorphic_strings(self):
        self.assertTrue(is_Isomorphic("egg", "add"))

    def test_non_isomorphic_strings(self):
        self.assertFalse(is_Isomorphic("foo", "bar"))

    def test_isomorphic_strings_with_spaces(self):
        self.assertTrue(is_Isomorphic("egg egg", "add add"))

    def test_non_isomorphic_strings_with_spaces(self):
        self.assertFalse(is_Isomorphic("foo bar", "hello world"))

    def test_isomorphic_strings_with_punctuation(self):
        self.assertTrue(is_Isomorphic("egg,egg", "add,add"))

    def test_non_isomorphic_strings_with_punctuation(self):
        self.assertFalse(is_Isomorphic("foo,bar", "hello,world"))

    def test_empty_strings(self):
        self.assertTrue(is_Isomorphic("", ""))

    def test_single_character_strings(self):
        self.assertTrue(is_Isomorphic("a", "a"))

    def test_isomorphic_strings_with_duplicates(self):
        self.assertTrue(is_Isomorphic("abab", "cdcd"))

    def test_non_isomorphic_strings_with_duplicates(self):
        self.assertFalse(is_Isomorphic("abab", "cded"))
