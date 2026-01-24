import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_dirty_chars("Hello, World!", "World"), "Hello,!")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_dirty_chars("", ""), "")

    def test_edge_case_empty_second_string(self):
        self.assertEqual(remove_dirty_chars("Hello, World!", ""), "Hello, World!")

    def test_edge_case_single_char_second_string(self):
        self.assertEqual(remove_dirty_chars("Hello, World!", "H"), "Hello, World!")

    def test_edge_case_multiple_chars_second_string(self):
        self.assertEqual(remove_dirty_chars("Hello, World!", "HW"), "Hello, World!")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            remove_dirty_chars(123, "World")

    def test_invalid_input_non_string_second(self):
        with self.assertRaises(TypeError):
            remove_dirty_chars("Hello, World!", 123)
