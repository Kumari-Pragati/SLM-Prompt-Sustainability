import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(remove_dirty_chars("", ""), "")
        self.assertEqual(remove_dirty_chars("", "a"), "")

    def test_single_char_strings(self):
        self.assertEqual(remove_dirty_chars("a", "a"), "a")
        self.assertEqual(remove_dirty_chars("a", "b"), "a")

    def test_common_strings(self):
        self.assertEqual(remove_dirty_chars("abc", "xyz"), "abc")
        self.assertEqual(remove_dirty_chars("xyz", "abc"), "")

    def test_overlapping_chars(self):
        self.assertEqual(remove_dirty_chars("abcd", "ab"), "cd")
        self.assertEqual(remove_dirty_chars("abcd", "cd"), "ab")

    def test_edge_cases(self):
        self.assertEqual(remove_dirty_chars("\x00abc", "xyz"), "abc")
        self.assertEqual(remove_dirty_chars("abc\uffff", "xyz"), "abc")
        self.assertEqual(remove_dirty_chars("abc", "\x7fxyz"), "abc")
        self.assertEqual(remove_dirty_chars("abc", "xyz\uffff"), "abc")

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            remove_dirty_chars(1, "a")
        with self.assertRaises(TypeError):
            remove_dirty_chars("a", 1)
