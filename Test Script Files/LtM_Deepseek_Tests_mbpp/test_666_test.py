import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_char("hello", "l"), 2)

    def test_empty_string(self):
        self.assertEqual(count_char("", "a"), 0)

    def test_char_not_in_string(self):
        self.assertEqual(count_char("hello", "z"), 0)

    def test_case_sensitivity(self):
        self.assertEqual(count_char("Hello", "h"), 0)

    def test_whitespace_in_string(self):
        self.assertEqual(count_char("hello world", "o"), 2)

    def test_special_characters(self):
        self.assertEqual(count_char("hello@world", "@"), 1)

    def test_count_char_with_multiple_occurrences(self):
        self.assertEqual(count_char("aabbcc", "b"), 2)
