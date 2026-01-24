import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_repeated_char_in_string(self):
        self.assertEqual(first_repeated_char('abcabc'), 'a')
        self.assertEqual(first_repeated_char('abcdefg'), 'None')
        self.assertEqual(first_repeated_char('aabbcc'), 'a')
        self.assertEqual(first_repeated_char('123123'), '1')
        self.assertEqual(first_repeated_char('abcdeff'), 'f')

    def test_empty_string(self):
        self.assertEqual(first_repeated_char(''), 'None')

    def test_string_with_one_char(self):
        self.assertEqual(first_repeated_char('a'), 'None')

    def test_string_with_repeated_chars(self):
        self.assertEqual(first_repeated_char('aabbccdd'), 'a')
        self.assertEqual(first_repeated_char('abcdabcd'), 'a')
        self.assertEqual(first_repeated_char('abcabcabc'), 'a')
        self.assertEqual(first_repeated_char('abcdabcdabcd'), 'a')
