import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_dirty_chars("hello world", "l"), "heo word")

    def test_empty_string(self):
        self.assertEqual(remove_dirty_chars("", ""), "")

    def test_no_dirty_chars(self):
        self.assertEqual(remove_dirty_chars("hello world", "abc"), "hello world")

    def test_all_dirty_chars(self):
        self.assertEqual(remove_dirty_chars("hello world", "abcdefghijklmnopqrstuvwxyz "), "")

    def test_repeated_dirty_chars(self):
        self.assertEqual(remove_dirty_chars("hello world", "l"), "heo word")

    def test_case_sensitivity(self):
        self.assertEqual(remove_dirty_chars("Hello World", "l"), "Heo Word")

    def test_single_dirty_char(self):
        self.assertEqual(remove_dirty_chars("hello world", "d"), "hello worl")

    def test_multiple_dirty_chars(self):
        self.assertEqual(remove_dirty_chars("hello world", "lo"), "he word")

    def test_edge_cases(self):
        self.assertEqual(remove_dirty_chars("a", "a"), "")
        self.assertEqual(remove_dirty_chars("", "a"), "")
