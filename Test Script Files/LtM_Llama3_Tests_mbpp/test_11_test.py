import unittest
from mbpp_11_code import remove_Occ

class TestRemove_Occ(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_Occ("hello", "o"), "hell")
        self.assertEqual(remove_Occ("world", "d"), "worl")
        self.assertEqual(remove_Occ("abc", "a"), "bc")

    def test_edge(self):
        self.assertEqual(remove_Occ("", "a"), "")
        self.assertEqual(remove_Occ("a", "a"), "")
        self.assertEqual(remove_Occ("abc", "c"), "ab")

    def test_edge2(self):
        self.assertEqual(remove_Occ("abc", "b"), "ac")
        self.assertEqual(remove_Occ("abc", "c"), "ab")
        self.assertEqual(remove_Occ("abc", "a"), "bc")

    def test_invalid(self):
        with self.assertRaises(TypeError):
            remove_Occ(123, "a")
        with self.assertRaises(TypeError):
            remove_Occ("abc", 123)
