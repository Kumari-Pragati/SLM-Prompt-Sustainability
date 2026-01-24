import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(remove_Char("abc", "a"), "bc")
        self.assertEqual(remove_Char("aaa", "a"), "")
        self.assertEqual(remove_Char("abca", "a"), "bc")
        self.assertEqual(remove_Char("abca", "c"), "ab")

    def test_edge_cases(self):
        self.assertEqual(remove_Char("", "a"), "")
        self.assertEqual(remove_Char("a", "a"), "")
        self.assertEqual(remove_Char("aa", "b"), "aa")
        self.assertEqual(remove_Char("aabb", "b"), "aa")

    def test_complex_cases(self):
        self.assertEqual(remove_Char("aabbccaa", "c"), "aabbaa")
        self.assertEqual(remove_Char("aabbccaa", "a"), "bcb")
        self.assertEqual(remove_Char("aabbccaa", "b"), "accaa")
