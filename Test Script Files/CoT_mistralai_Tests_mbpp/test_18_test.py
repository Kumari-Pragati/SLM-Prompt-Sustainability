import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(remove_dirty_chars("", "a"), "")
        self.assertEqual(remove_dirty_chars("a", ""), "a")

    def test_single_char_strings(self):
        self.assertEqual(remove_dirty_chars("a", "a"), "a")
        self.assertEqual(remove_dirty_chars("A", "a"), "")

    def test_multiple_chars_strings(self):
        self.assertEqual(remove_dirty_chars("abc", "xyz"), "abc")
        self.assertEqual(remove_dirty_chars("xyz", "abc"), "")

    def test_case_sensitivity(self):
        self.assertEqual(remove_dirty_chars("ABC", "abc"), "ABC")
        self.assertEqual(remove_dirty_chars("abc", "ABC"), "")

    def test_multiple_occurrences(self):
        self.assertEqual(remove_dirty_chars("aaa", "bbb"), "aaa")
        self.assertEqual(remove_dirty_chars("bbb", "aaa"), "")

    def test_longer_string_with_fewer_chars(self):
        self.assertEqual(remove_dirty_chars("abcdefghijklmnopqrstuvwxyz", "ABC"), "abcdefghijklmnopqrstuvwxyz")

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, remove_dirty_chars, 1, "a")
        self.assertRaises(TypeError, remove_dirty_chars, "a", 1)
