import unittest
from mbpp_885_code import is_Isomorphic

class TestIsIsomorphic(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertTrue(is_Isomorphic("abc", "def"))
        self.assertTrue(is_Isomorphic("abc", "abc"))
        self.assertTrue(is_Isomorphic("abc", "abcde"))

    def test_edge_cases(self):
        self.assertFalse(is_Isomorphic("", ""))
        self.assertFalse(is_Isomorphic("abc", ""))
        self.assertFalse(is_Isomorphic("", "abc"))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Isomorphic(123, "abc")
        with self.assertRaises(TypeError):
            is_Isomorphic("abc", 123)

    def test_more_complex_inputs(self):
        self.assertFalse(is_Isomorphic("abc", "defgh"))
        self.assertFalse(is_Isomorphic("abc", "defabc"))
