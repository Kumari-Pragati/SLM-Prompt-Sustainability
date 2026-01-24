import unittest

from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_dirty_chars("hello world", "e"), "hllo world")

    def test_edge_case(self):
        self.assertEqual(remove_dirty_chars("", "e"), "")
        self.assertEqual(remove_dirty_chars("hello world", ""), "hello world")

    def test_corner_case(self):
        self.assertEqual(remove_dirty_chars("aabbcc", "abc"), "")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_dirty_chars(123, "e")
        with self.assertRaises(TypeError):
            remove_dirty_chars("hello world", 123)
