import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(remove_dirty_chars("hello world", "l"), "heo word")
        self.assertEqual(remove_dirty_chars("programming", "g"), "proamming")
        self.assertEqual(remove_dirty_chars("abc", ""), "abc")

    def test_edge_cases(self):
        self.assertEqual(remove_dirty_chars("", "a"), "")
        self.assertEqual(remove_dirty_chars("a", "a"), "")
        self.assertEqual(remove_dirty_chars("abc", "abc"), "")

    def test_boundary_conditions(self):
        self.assertEqual(remove_dirty_chars("a" * 1000, "a"), "" * 1000)
        self.assertEqual(remove_dirty_chars("b" * 1000, "a"), "b" * 1000)

    def test_corner_cases(self):
        self.assertEqual(remove_dirty_chars("abcabc", "abc"), "")
        self.assertEqual(remove_dirty_chars("abcabc", "b"), "acac")
