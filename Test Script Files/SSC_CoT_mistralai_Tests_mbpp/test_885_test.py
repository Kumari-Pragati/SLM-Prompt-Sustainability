import unittest
from mbpp_885_code import is_Isomorphic

class TestIsomorphic(unittest.TestCase):

    def test_isomorphic_strings(self):
        self.assertTrue(is_Isomorphic("aba", "cdc"))
        self.assertTrue(is_Isomorphic("ab", "aa"))
        self.assertTrue(is_Isomorphic("eidetikon", "koniutedie"))

    def test_not_isomorphic_strings(self):
        self.assertFalse(is_Isomorphic("aba", "abd"))
        self.assertFalse(is_Isomorphic("ab", "ac"))
        self.assertFalse(is_Isomorphic("eidetikon", "koniutedik"))

    def test_empty_strings(self):
        self.assertTrue(is_Isomorphic("", ""))
        self.assertFalse(is_Isomorphic("", "a"))
        self.assertFalse(is_Isomorphic("a", ""))

    def test_single_char_strings(self):
        self.assertTrue(is_Isomorphic("a", "a"))
        self.assertFalse(is_Isomorphic("a", "b"))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Isomorphic(1, 2)
        with self.assertRaises(TypeError):
            is_Isomorphic([], [])
