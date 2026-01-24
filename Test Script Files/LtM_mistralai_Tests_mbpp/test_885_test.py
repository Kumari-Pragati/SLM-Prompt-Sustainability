import unittest
from mbpp_885_code import is_Isomorphic

class TestIsomorphic(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(is_Isomorphic("aba", "cdc"))
        self.assertTrue(is_Isomorphic("egg", "add"))

    def test_edge_cases(self):
        self.assertFalse(is_Isomorphic("a", "b"))
        self.assertFalse(is_Isomorphic("", ""))
        self.assertFalse(is_Isomorphic("abc", "abcd"))
        self.assertFalse(is_Isomorphic("123", "456"))

    def test_complex(self):
        self.assertTrue(is_Isomorphic("ababcbab", "acdcadcd"))
        self.assertFalse(is_Isomorphic("ababcbab", "acdcdcdc"))
        self.assertTrue(is_Isomorphic("abcd", "UUUU"))
        self.assertFalse(is_Isomorphic("abcd", "UUUUU"))
