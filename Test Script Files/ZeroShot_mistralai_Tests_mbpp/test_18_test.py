import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(remove_dirty_chars("", "abc"), "")
        self.assertEqual(remove_dirty_chars("abc", ""), "abc")

    def test_single_char_strings(self):
        self.assertEqual(remove_dirty_chars("a", "bc"), "a")
        self.assertEqual(remove_dirty_chars("b", "ac"), "b")
        self.assertEqual(remove_dirty_chars("c", "ab"), "c")

    def test_multiple_char_strings(self):
        self.assertEqual(remove_dirty_chars("abcd", "efgh"), "abcd")
        self.assertEqual(remove_dirty_chars("efgh", "abcd"), "abcd")
        self.assertEqual(remove_dirty_chars("abcdefgh", "ijk"), "abcdefgh")
        self.assertEqual(remove_dirty_chars("ijk", "abcdefgh"), "abcdefgh")

    def test_overlapping_chars(self):
        self.assertEqual(remove_dirty_chars("abcd", "cd"), "a")
        self.assertEqual(remove_dirty_chars("cd", "abcd"), "ab")
        self.assertEqual(remove_dirty_chars("abcdefgh", "hij"), "abcdef")
        self.assertEqual(remove_dirty_chars("hij", "abcdefgh"), "abcdefg")

    def test_same_chars(self):
        self.assertEqual(remove_dirty_chars("aa", "a"), "")
        self.assertEqual(remove_dirty_chars("aaa", "aa"), "")
        self.assertEqual(remove_dirty_chars("aaaa", "aaa"), "")

    def test_different_chars(self):
        self.assertEqual(remove_dirty_chars("abcd", "efghij"), "abcd")
        self.assertEqual(remove_dirty_chars("efghij", "abcd"), "abcd")
