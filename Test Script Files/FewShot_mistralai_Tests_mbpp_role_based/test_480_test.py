import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):
    def test_single_char(self):
        self.assertEqual(get_max_occuring_char('a'), 'a')

    def test_multiple_same_chars(self):
        self.assertEqual(get_max_occuring_char('aaaa'), 'a')

    def test_multiple_different_chars(self):
        self.assertEqual(get_max_occuring_char('abcdefg'), 'a')

    def test_empty_string(self):
        self.assertEqual(get_max_occuring_char(''), '')

    def test_all_spaces(self):
        self.assertEqual(get_max_occuring_char('   '), ' ')

    def test_single_space(self):
        self.assertEqual(get_max_occuring_char(' '), ' ')

    def test_string_with_non_ascii(self):
        self.assertRaises(ValueError, get_max_occuring_char, 'abc\u0304def')
