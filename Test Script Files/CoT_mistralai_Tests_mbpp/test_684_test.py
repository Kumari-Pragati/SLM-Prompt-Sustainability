import unittest
from mbpp_684_code import count_Char

class TestCountChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Char("", "a"), 0)

    def test_single_character(self):
        self.assertEqual(count_Char("a", "a"), 1)

    def test_multiple_characters(self):
        self.assertEqual(count_Char("abc", "a"), 1)
        self.assertEqual(count_Char("abc", "b"), 1)
        self.assertEqual(count_Char("abc", "c"), 1)

    def test_case_sensitivity(self):
        self.assertEqual(count_Char("ABC", "a"), 0)
        self.assertEqual(count_Char("ABC", "A"), 0)
        self.assertEqual(count_Char("abc", "A"), 0)
        self.assertEqual(count_Char("abc", "a"), 1)

    def test_long_string_and_single_char(self):
        long_string = "a" * 100
        self.assertEqual(count_Char(long_string, "a"), 100)

    def test_long_string_and_multiple_chars(self):
        long_string = "abc" * 33
        self.assertEqual(count_Char(long_string, "a"), 33)
        self.assertEqual(count_Char(long_string, "b"), 33)
        self.assertEqual(count_Char(long_string, "c"), 33)

    def test_single_char_in_long_string(self):
        long_string = "a" * 100 + "b"
        self.assertEqual(count_Char(long_string, "a"), 100)
        self.assertEqual(count_Char(long_string, "b"), 1)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            count_Char("abc", -1)

    def test_empty_char(self):
        with self.assertRaises(ValueError):
            count_Char("abc", "")
