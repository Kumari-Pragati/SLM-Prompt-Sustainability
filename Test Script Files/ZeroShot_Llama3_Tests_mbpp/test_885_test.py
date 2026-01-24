import unittest
from mbpp_885_code import is_Isomorphic

class TestIsomorphic(unittest.TestCase):

    def test_isomorphic(self):
        self.assertTrue(is_Isomorphic("egg", "add"))
        self.assertFalse(is_Isomorphic("foo", "bar"))
        self.assertTrue(is_Isomorphic("paper", "title"))
        self.assertFalse(is_Isomorphic("hello", "world"))
        self.assertTrue(is_Isomorphic("abba", "model"))
        self.assertFalse(is_Isomorphic("abc", "def"))

    def test_isomorphic_empty(self):
        self.assertFalse(is_Isomorphic("", ""))
        self.assertFalse(is_Isomorphic("", "abc"))
        self.assertFalse(is_Isomorphic("abc", ""))

    def test_isomorphic_single_char(self):
        self.assertTrue(is_Isomorphic("a", "a"))
        self.assertFalse(is_Isomorphic("a", "b"))
