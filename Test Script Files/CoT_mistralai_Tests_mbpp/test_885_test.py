import unittest
from mbpp_885_code import is_Isomorphic

class TestIsomorphic(unittest.TestCase):
    def test_isomorphic_strings(self):
        self.assertTrue(is_Isomorphic("aba", "bba"))
        self.assertTrue(is_Isomorphic("abcd", "cdab"))
        self.assertTrue(is_Isomorphic("abcd", "abcd"))

    def test_non_isomorphic_strings(self):
        self.assertFalse(is_Isomorphic("aba", "abaa"))
        self.assertFalse(is_Isomorphic("abcd", "acdb"))
        self.assertFalse(is_Isomorphic("abcd", "abxz"))

    def test_empty_strings(self):
        self.assertTrue(is_Isomorphic("", ""))
        self.assertFalse(is_Isomorphic("", "a"))
        self.assertFalse(is_Isomorphic("a", ""))

    def test_single_character_strings(self):
        self.assertTrue(is_Isomorphic("a", "a"))
        self.assertFalse(is_Isomorphic("a", "b"))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_Isomorphic, 1, 2)
        self.assertRaises(TypeError, is_Isomorphic, [1, 2, 3], [4, 5, 6])
