import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_char('aabbbcc'), 'b')

    def test_single_character(self):
        self.assertEqual(max_char('a'), 'a')

    def test_empty_string(self):
        self.assertIsNone(max_char(''))

    def test_all_same_characters(self):
        self.assertEqual(max_char('aaaaa'), 'a')

    def test_case_sensitivity(self):
        self.assertEqual(max_char('aAaAaA'), 'a')

    def test_whitespace(self):
        self.assertEqual(max_char('a b c'), ' ')

    def test_numeric_characters(self):
        self.assertEqual(max_char('12312323'), '3')

    def test_special_characters(self):
        self.assertEqual(max_char('!@#!@#!@'), '!')
