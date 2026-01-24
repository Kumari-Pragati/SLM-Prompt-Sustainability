import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_dirty_chars("hello world", "l"), "heo word")

    def test_no_dirty_chars(self):
        self.assertEqual(remove_dirty_chars("hello world", "abc"), "hello world")

    def test_empty_strings(self):
        self.assertEqual(remove_dirty_chars("", ""), "")

    def test_all_dirty_chars(self):
        self.assertEqual(remove_dirty_chars("hello world", "abcdefghijklmnopqrstuvwxyz "), "")

    def test_single_dirty_char(self):
        self.assertEqual(remove_dirty_chars("hello world", "o"), "hell wrld")

    def test_repeated_dirty_chars(self):
        self.assertEqual(remove_dirty_chars("hello world", "l"), "heo word")

    def test_case_sensitivity(self):
        self.assertEqual(remove_dirty_chars("Hello World", "l"), "Heo Word")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            remove_dirty_chars(123, "l")
        with self.assertRaises(TypeError):
            remove_dirty_chars("hello world", 123)
