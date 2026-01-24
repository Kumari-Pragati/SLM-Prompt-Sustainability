import unittest
from mbpp_885_code import is_Isomorphic

class TestIsIsomorphic(unittest.TestCase):
    def test_isomorphic_strings(self):
        self.assertTrue(is_Isomorphic("abc", "123"))
        self.assertTrue(is_Isomorphic("abcd", "xyzq"))

    def test_empty_strings(self):
        self.assertTrue(is_Isomorphic("", ""))

    def test_single_character_strings(self):
        self.assertTrue(is_Isomorphic("a", "a"))
        self.assertFalse(is_Isomorphic("a", "b"))

    def test_identical_strings(self):
        self.assertTrue(is_Isomorphic("abc", "abc"))

    def test_different_lengths(self):
        self.assertFalse(is_Isomorphic("abc", "abcd"))

    def test_non_string_inputs(self):
        self.assertRaises(TypeError, is_Isomorphic, 123, 456)
        self.assertRaises(TypeError, is_Isomorphic, [1, 2, 3], [4, 5, 6])
