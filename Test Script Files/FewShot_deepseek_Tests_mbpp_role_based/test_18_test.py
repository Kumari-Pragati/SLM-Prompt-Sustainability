import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_dirty_chars("hello world", "l"), "heo word")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_dirty_chars("", "l"), "")

    def test_boundary_case_single_char(self):
        self.assertEqual(remove_dirty_chars("a", "a"), "")
        self.assertEqual(remove_dirty_chars("a", "b"), "a")

    def test_boundary_case_multiple_chars(self):
        self.assertEqual(remove_dirty_chars("hello", "lo"), "he")
        self.assertEqual(remove_dirty_chars("hello", "he"), "llo")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_dirty_chars(123, "l")
        with self.assertRaises(TypeError):
            remove_dirty_chars("hello world", 123)
