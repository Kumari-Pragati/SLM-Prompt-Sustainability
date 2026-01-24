import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):
    def test_remove_single_dirty_char(self):
        dirty_chars = "a" * 10 + "b" * 10
        clean_string = "a" * 10
        result = remove_dirty_chars(clean_string, dirty_chars)
        self.assertEqual(result, clean_string)

    def test_remove_multiple_dirty_chars(self):
        dirty_chars = "a" * 10 + "b" * 10 + "c" * 10
        clean_string = "a" * 10 + "d" * 10
        result = remove_dirty_chars(clean_string, dirty_chars)
        self.assertEqual(result, "a" * 10 + "d" * 10)

    def test_remove_all_chars(self):
        dirty_chars = "a" * 256
        clean_string = ""
        result = remove_dirty_chars(clean_string, dirty_chars)
        self.assertEqual(result, "")

    def test_empty_strings(self):
        dirty_chars = ""
        clean_string = ""
        result = remove_dirty_chars(clean_string, dirty_chars)
        self.assertEqual(result, "")

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            remove_dirty_chars(123, "abc")

    def test_invalid_input_chars(self):
        with self.assertRaises(TypeError):
            remove_dirty_chars("abc", 123)
