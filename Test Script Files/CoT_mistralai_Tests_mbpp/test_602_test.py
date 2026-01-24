import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(first_repeated_char(""), "None")

    def test_single_char_string(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(first_repeated_char(char), char)

    def test_no_repeated_char_string(self):
        self.assertEqual(first_repeated_char("zyxwvutsrqponmlkjihgfedcba"), "None")

    def test_repeated_char_at_beginning(self):
        self.assertEqual(first_repeated_char("aa"), "a")

    def test_repeated_char_in_middle(self):
        self.assertEqual(first_repeated_char("abcacc"), "c")

    def test_repeated_char_at_end(self):
        self.assertEqual(first_repeated_char("abcxx"), "x")

    def test_repeated_char_multiple_times(self):
        self.assertEqual(first_repeated_char("aaa"), "a")

    def test_repeated_char_after_non_repeated_chars(self):
        self.assertEqual(first_repeated_char("abcxx"), "x")

    def test_repeated_char_with_whitespace(self):
        self.assertEqual(first_repeated_char("hello world"), " ")

    def test_repeated_char_with_special_characters(self):
        self.assertEqual(first_repeated_char("!@#$%^&*()_+-=[]{}|;':\"<>,.?/"), "!")

    def test_invalid_input_empty_list(self):
        with self.assertRaises(TypeError):
            first_repeated_char([])

    def test_invalid_input_none_type(self):
        with self.assertRaises(TypeError):
            first_repeated_char(None)
