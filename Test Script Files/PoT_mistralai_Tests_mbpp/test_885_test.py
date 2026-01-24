import unittest
from mbpp_885_code import is_Isomorphic

class TestIsomorphic(unittest.TestCase):
    def test_isomorphic_strings(self):
        self.assertTrue(is_Isomorphic("abc", "def"))
        self.assertTrue(is_Isomorphic("abcd", "abcd"))
        self.assertTrue(is_Isomorphic("aabb", "abbA"))

    def test_non_isomorphic_strings(self):
        self.assertFalse(is_Isomorphic("abc", "acb"))
        self.assertFalse(is_Isomorphic("abcd", "acbd"))
        self.assertFalse(is_Isomorphic("aabb", "baab"))

    def test_empty_strings(self):
        self.assertTrue(is_Isomorphic("", ""))
        self.assertFalse(is_Isomorphic("", "a"))
        self.assertFalse(is_Isomorphic("a", ""))

    def test_single_char_strings(self):
        self.assertTrue(is_Isomorphic("a", "a"))
        self.assertFalse(is_Isomorphic("a", "b"))

    def test_different_lengths(self):
        self.assertFalse(is_Isomorphic("abc", "abcd"))
        self.assertFalse(is_Isomorphic("abcd", "abc"))
