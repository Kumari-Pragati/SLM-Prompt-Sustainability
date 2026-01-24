import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_char("hello", "l"), 2)

    def test_single_char(self):
        self.assertEqual(count_char("aaaaa", "a"), 5)

    def test_char_not_in_string(self):
        self.assertEqual(count_char("hello", "z"), 0)

    def test_empty_string(self):
        self.assertEqual(count_char("", "a"), 0)

    def test_case_sensitivity(self):
        self.assertEqual(count_char("Hello", "h"), 0)

    def test_whitespace(self):
        self.assertEqual(count_char("hello world", " "), 1)

    def test_special_characters(self):
        self.assertEqual(count_char("hello@world", "@"), 1)

    def test_numeric_characters(self):
        self.assertEqual(count_char("123456", "3"), 1)
