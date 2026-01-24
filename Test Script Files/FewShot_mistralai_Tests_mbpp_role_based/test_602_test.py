import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):
    def test_single_char_string(self):
        self.assertEqual(first_repeated_char("a"), "a")

    def test_empty_string(self):
        self.assertEqual(first_repeated_char(""), "None")

    def test_no_repeated_char(self):
        self.assertEqual(first_repeated_char("abc"), "None")

    def test_repeated_char_at_beginning(self):
        self.assertEqual(first_repeated_char("aa"), "a")

    def test_repeated_char_in_middle(self):
        self.assertEqual(first_repeated_char("abcdea"), "a")

    def test_repeated_char_at_end(self):
        self.assertEqual(first_repeated_char("abcxa"), "x")

    def test_repeated_char_multiple_times(self):
        self.assertEqual(first_repeated_char("aaa"), "a")

    def test_repeated_char_with_spaces(self):
        self.assertEqual(first_repeated_char("hello world"), " ")
