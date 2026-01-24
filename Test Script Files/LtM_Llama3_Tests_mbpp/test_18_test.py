import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_dirty_chars("", ""), "")

    def test_single_char_string(self):
        self.assertEqual(remove_dirty_chars("a", "a"), "a")

    def test_multiple_char_string(self):
        self.assertEqual(remove_dirty_chars("abc", "abc"), "abc")

    def test_second_string_empty(self):
        self.assertEqual(remove_dirty_chars("abc", ""), "")

    def test_second_string_single_char(self):
        self.assertEqual(remove_dirty_chars("abc", "a"), "abc")

    def test_second_string_multiple_char(self):
        self.assertEqual(remove_dirty_chars("abc", "abc"), "abc")

    def test_second_string_all_chars(self):
        self.assertEqual(remove_dirty_chars("abc", "abcabc"), "abc")

    def test_second_string_no_chars(self):
        self.assertEqual(remove_dirty_chars("abc", "def"), "abc")

    def test_second_string_all_chars_and_no_chars(self):
        self.assertEqual(remove_dirty_chars("abc", "abcdef"), "abc")

    def test_second_string_all_chars_and_no_chars_reversed(self):
        self.assertEqual(remove_dirty_chars("abc", "defabc"), "abc")
