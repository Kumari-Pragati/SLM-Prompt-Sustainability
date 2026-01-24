import unittest
from mbpp_885_code import is_Isomorphic

class TestIsomorphic(unittest.TestCase):
    def test_isomorphic_strings(self):
        self.assertTrue(is_Isomorphic("egg", "add"))

    def test_non_isomorphic_strings(self):
        self.assertFalse(is_Isomorphic("abc", "def"))

    def test_empty_strings(self):
        self.assertFalse(is_Isomorphic("", ""))

    def test_single_character_strings(self):
        self.assertTrue(is_Isomorphic("a", "a"))
        self.assertFalse(is_Isomorphic("a", "b"))

    def test_non_string_inputs(self):
        with self.assertRaises(TypeError):
            is_Isomorphic(123, "abc")
