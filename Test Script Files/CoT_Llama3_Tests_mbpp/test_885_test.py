import unittest
from mbpp_885_code import is_Isomorphic

class TestIsIsomorphic(unittest.TestCase):
    def test_isomorphic_strings(self):
        self.assertTrue(is_Isomorphic("egg", "add"))
        self.assertTrue(is_Isomorphic("foo", "bar"))
        self.assertFalse(is_Isomorphic("hello", "world"))

    def test_non_isomorphic_strings(self):
        self.assertFalse(is_Isomorphic("abc", "def"))
        self.assertFalse(is_Isomorphic("hello", "goodbye"))

    def test_empty_strings(self):
        self.assertTrue(is_Isomorphic("", ""))
        self.assertFalse(is_Isomorphic("", "hello"))

    def test_single_character_strings(self):
        self.assertTrue(is_Isomorphic("a", "a"))
        self.assertFalse(is_Isomorphic("a", "b"))

    def test_isomorphic_strings_with_spaces(self):
        self.assertTrue(is_Isomorphic("hello world", "goodbye world"))
