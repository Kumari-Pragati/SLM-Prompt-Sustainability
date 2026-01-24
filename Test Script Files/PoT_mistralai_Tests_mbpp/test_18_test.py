import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(remove_dirty_chars("", "a"), "")
        self.assertEqual(remove_dirty_chars("a", ""), "a")

    def test_single_char_strings(self):
        self.assertEqual(remove_dirty_chars("a", "a"), "a")
        self.assertEqual(remove_dirty_chars("A", "a"), "")
        self.assertEqual(remove_dirty_chars("a", "A"), "a")

    def test_multiple_chars_strings(self):
        self.assertEqual(remove_dirty_chars("abc", "xyz"), "abc")
        self.assertEqual(remove_dirty_chars("xyz", "abc"), "")
        self.assertEqual(remove_dirty_chars("abc", "ABC"), "a")
        self.assertEqual(remove_dirty_chars("ABC", "abc"), "A")
        self.assertEqual(remove_dirty_chars("abc", "ABCdef"), "a")
        self.assertEqual(remove_dirty_chars("ABCdef", "abc"), "A")

    def test_different_length_strings(self):
        self.assertEqual(remove_dirty_chars("abc", "xyzdef"), "abc")
        self.assertEqual(remove_dirty_chars("xyzdef", "abc"), "")

    def test_repeated_chars(self):
        self.assertEqual(remove_dirty_chars("aaa", "a"), "a")
        self.assertEqual(remove_dirty_chars("aaa", "aa"), "a")
        self.assertEqual(remove_dirty_chars("aaa", "aaa"), "a")
