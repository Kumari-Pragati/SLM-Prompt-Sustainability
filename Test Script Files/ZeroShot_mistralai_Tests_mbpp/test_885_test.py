import unittest
from mbpp_885_code import is_Isomorphic

class TestIsomorphic(unittest.TestCase):

    def test_is_isomorphic_simple(self):
        self.assertTrue(is_Isomorphic("aba", "cdc"))
        self.assertTrue(is_Isomorphic("egg", "add"))
        self.assertTrue(is_Isomorphic("foo", "bar"))

    def test_is_isomorphic_complex(self):
        self.assertFalse(is_Isomorphic("abab", "cdcd"))
        self.assertFalse(is_Isomorphic("abcd", "cdab"))
        self.assertFalse(is_Isomorphic("abc", "acb"))

    def test_is_isomorphic_empty(self):
        self.assertTrue(is_Isomorphic("", ""))
        self.assertTrue(is_Isomorphic(" ", " "))
