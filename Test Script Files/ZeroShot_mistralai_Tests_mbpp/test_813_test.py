import unittest
from mbpp_813_code import string_length

class TestStringLength(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(string_length(''), 0)

    def test_single_character_string(self):
        self.assertEqual(string_length('a'), 1)
        self.assertEqual(string_length('b'), 1)
        self.assertEqual(string_length('c'), 1)

    def test_multiple_character_strings(self):
        self.assertEqual(string_length('abc'), 3)
        self.assertEqual(string_length('def'), 3)
        self.assertEqual(string_length('ghi'), 3)

    def test_long_string(self):
        long_string = 'abcdefghijklmnopqrstuvwxyz'
        self.assertEqual(string_length(long_string), 26)

    def test_special_characters(self):
        self.assertEqual(string_length('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), 32)
        self.assertEqual(string_length('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 26)
        self.assertEqual(string_length('1234567890'), 10)
