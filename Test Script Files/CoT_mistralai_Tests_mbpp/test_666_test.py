import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_char("", "a"), 0)

    def test_single_char_string(self):
        self.assertEqual(count_char("a", "a"), 1)

    def test_multiple_chars_string(self):
        self.assertEqual(count_char("abc", "a"), 1)
        self.assertEqual(count_char("abc", "b"), 1)
        self.assertEqual(count_char("abc", "c"), 1)

    def test_case_insensitive(self):
        self.assertEqual(count_char("ABC", "a"), 1)
        self.assertEqual(count_char("ABC", "b"), 1)
        self.assertEqual(count_char("ABC", "C"), 1)

    def test_long_string(self):
        long_string = "x" * 1000
        self.assertEqual(count_char(long_string, "x"), 1000)

    def test_single_char_in_long_string(self):
        long_string = "abcdefghijklmnopqrstuvwxyz" * 10
        self.assertEqual(count_char(long_string, "a"), 10)

    def test_non_string_input(self):
        self.assertRaises(TypeError, count_char, 123, "a")
        self.assertRaises(TypeError, count_char, "abc", 123)
