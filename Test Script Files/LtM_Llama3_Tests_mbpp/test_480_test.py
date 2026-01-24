import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(get_max_occuring_char("a"), 'a')
        self.assertEqual(get_max_occuring_char("b"), 'b')
        self.assertEqual(get_max_occuring_char("c"), 'c')

    def test_empty_string(self):
        self.assertEqual(get_max_occuring_char(""), '')

    def test_single_char(self):
        self.assertEqual(get_max_occuring_char("a"), 'a')
        self.assertEqual(get_max_occuring_char("b"), 'b')
        self.assertEqual(get_max_occuring_char("c"), 'c')

    def test_multiple_chars(self):
        self.assertEqual(get_max_occuring_char("abc"), 'a')
        self.assertEqual(get_max_occuring_char("bca"), 'b')
        self.assertEqual(get_max_occuring_char("cab"), 'c')

    def test_max_occuring_char(self):
        self.assertEqual(get_max_occuring_char("aaa"), 'a')
        self.assertEqual(get_max_occuring_char("bbb"), 'b')
        self.assertEqual(get_max_occuring_char("ccc"), 'c')

    def test_non_ascii_chars(self):
        self.assertEqual(get_max_occuring_char("abc"), 'a')
        self.assertEqual(get_max_occuring_char("bca"), 'b')
        self.assertEqual(get_max_occuring_char("cab"), 'c')

    def test_non_ascii_chars_with_spaces(self):
        self.assertEqual(get_max_occuring_char("abc "), 'a')
        self.assertEqual(get_max_occuring_char("bca "), 'b')
        self.assertEqual(get_max_occuring_char("cab "), 'c')
