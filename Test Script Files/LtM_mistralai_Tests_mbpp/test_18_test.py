import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(remove_dirty_chars("Hello", "abc"), "Hello")

    def test_case_with_common_chars(self):
        self.assertEqual(remove_dirty_chars("HelloWorld", "abcdefghijklmnopqrstuvwxyz"), "HelloWorld")

    def test_case_with_single_char(self):
        self.assertEqual(remove_dirty_chars("a", "bcd"), "")

    def test_case_with_empty_strings(self):
        self.assertEqual(remove_dirty_chars("", "abc"), "")
        self.assertEqual(remove_dirty_chars("abc", ""), "")

    def test_case_with_long_strings(self):
        long_string = "a" * 255
        self.assertEqual(remove_dirty_chars(long_string, "z"), long_string)

    def test_case_with_invalid_chars(self):
        self.assertEqual(remove_dirty_chars("Hello\nWorld", "abcdefghijklmnopqrstuvwxyz"), "HelloWorld")
