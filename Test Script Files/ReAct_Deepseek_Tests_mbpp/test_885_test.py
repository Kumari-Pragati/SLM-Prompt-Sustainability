import unittest
from mbpp_885_code import is_Isomorphic

class TestIsIsomorphic(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_Isomorphic("egg", "add"))
        self.assertTrue(is_Isomorphic("paper", "title"))
        self.assertFalse(is_Isomorphic("foo", "bar"))

    def test_edge_cases(self):
        self.assertTrue(is_Isomorphic("", ""))
        self.assertFalse(is_Isomorphic("a", ""))
        self.assertFalse(is_Isomorphic("", "a"))

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            is_Isomorphic(123, "abc")
        with self.assertRaises(TypeError):
            is_Isomorphic("abc", 123)
        with self.assertRaises(TypeError):
            is_Isomorphic(123, 456)
