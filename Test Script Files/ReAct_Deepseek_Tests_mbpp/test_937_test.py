import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_char('aabbbcc'), 'b')

    def test_single_character(self):
        self.assertEqual(max_char('aaaaa'), 'a')

    def test_empty_string(self):
        self.assertIsNone(max_char(''))

    def test_string_with_spaces(self):
        self.assertEqual(max_char('a b c'), ' ')

    def test_string_with_numbers(self):
        self.assertEqual(max_char('1234561'), '1')

    def test_string_with_special_characters(self):
        self.assertEqual(max_char('!@#$%^&*('), '(')

    def test_string_with_equal_characters(self):
        self.assertEqual(max_char('abc'), 'a')
