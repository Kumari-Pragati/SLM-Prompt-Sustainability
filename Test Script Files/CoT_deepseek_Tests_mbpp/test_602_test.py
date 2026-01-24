import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_repeated_char('abcab'), 'a')
        self.assertEqual(first_repeated_char('abcabc'), 'a')
        self.assertEqual(first_repeated_char('abcdabc'), 'a')

    def test_single_char(self):
        self.assertEqual(first_repeated_char('a'), 'None')

    def test_no_repeat(self):
        self.assertEqual(first_repeated_char('abcdefg'), 'None')

    def test_empty_string(self):
        self.assertEqual(first_repeated_char(''), 'None')

    def test_repeated_at_end(self):
        self.assertEqual(first_repeated_char('abcddcba'), 'd')

    def test_repeated_at_start(self):
        self.assertEqual(first_repeated_char('abcabc'), 'a')

    def test_case_sensitivity(self):
        self.assertEqual(first_repeated_char('Abcabc'), 'a')

    def test_whitespace(self):
        self.assertEqual(first_repeated_char('abc abcab'), ' ')

    def test_special_characters(self):
        self.assertEqual(first_repeated_char('abc!abc'), '!')
