import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):
    def test_uppercase_char_position(self):
        self.assertEqual(count_char_position('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 26)

    def test_lowercase_char_position(self):
        self.assertEqual(count_char_position('abcdefghijklmnopqrstuvwxyz'), 26)

    def test_mixed_case_char_position(self):
        self.assertEqual(count_char_position('ABCabc'), 3)

    def test_empty_string(self):
        self.assertEqual(count_char_position(''), 0)

    def test_string_with_only_numbers(self):
        self.assertEqual(count_char_position('123456'), 0)

    def test_string_with_special_characters(self):
        self.assertEqual(count_char_position('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), 0)
