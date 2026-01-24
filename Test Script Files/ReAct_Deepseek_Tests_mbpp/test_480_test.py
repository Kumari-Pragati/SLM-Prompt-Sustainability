import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_max_occuring_char('aabbbcc'), 'b')

    def test_single_char_string(self):
        self.assertEqual(get_max_occuring_char('a'), 'a')

    def test_empty_string(self):
        self.assertEqual(get_max_occuring_char(''), '')

    def test_all_same_chars(self):
        self.assertEqual(get_max_occuring_char('aaaaa'), 'a')

    def test_all_different_chars(self):
        self.assertEqual(get_max_occuring_char('abc'), 'a')

    def test_large_string(self):
        self.assertEqual(get_max_occuring_char('a' * 10000 + 'b' * 9999 + 'c' * 10001), 'c')

    def test_string_with_spaces(self):
        self.assertEqual(get_max_occuring_char('a b c'), ' ')

    def test_string_with_numbers(self):
        self.assertEqual(get_max_occuring_char('123123'), '1')

    def test_string_with_special_chars(self):
        self.assertEqual(get_max_occuring_char('!@#!@#'), '!')
