import unittest
from mbpp_885_code import is_Isomorphic

class TestIsomorphic(unittest.TestCase):

    def test_isomorphic_same_length_strings(self):
        self.assertTrue(is_Isomorphic("abc", "def"))
        self.assertTrue(is_Isomorphic("aabb", "xyyx"))

    def test_isomorphic_different_lengths_strings(self):
        self.assertFalse(is_Isomorphic("abc", "abcd"))
        self.assertFalse(is_Isomorphic("aabb", "aab"))

    def test_isomorphic_empty_strings(self):
        self.assertTrue(is_Isomorphic("", ""))
        self.assertFalse(is_Isomorphic("", "a"))

    def test_isomorphic_single_char_strings(self):
        self.assertTrue(is_Isomorphic("a", "a"))
        self.assertFalse(is_Isomorphic("a", "b"))

    def test_isomorphic_special_characters(self):
        self.assertTrue(is_Isomorphic("ab#", "##ba"))
        self.assertFalse(is_Isomorphic("ab#", "##c"))

    def test_isomorphic_numbers(self):
        self.assertTrue(is_Isomorphic("123", "456"))
        self.assertFalse(is_Isomorphic("123", "124"))

    def test_isomorphic_mixed_types(self):
        self.assertRaises(TypeError, is_Isomorphic, "abc", 123)
        self.assertRaises(TypeError, is_Isomorphic, 123, "abc")
