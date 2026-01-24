import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(max_char(''), '')

    def test_single_character_string(self):
        self.assertEqual(max_char('a'), 'a')

    def test_multiple_characters_string(self):
        self.assertEqual(max_char('abcdefghijklmnopqrstuvwxyz'), 'z')

    def test_case_insensitive(self):
        self.assertEqual(max_char('ABC'), 'C')

    def test_repeated_characters(self):
        self.assertEqual(max_char('aaaabbbbcccc'), 'c')

    def test_string_with_numbers(self):
        self.assertEqual(max_char('abc123def'), 'e')

    def test_string_with_special_characters(self):
        self.assertEqual(max_char('abc!@#$%^&*()_+'), '*')

    def test_string_with_whitespace(self):
        self.assertEqual(max_char('abc def'), ' ')

    def test_string_with_only_whitespace(self):
        self.assertEqual(max_char('   '), ' ')

    def test_string_with_only_numbers(self):
        self.assertEqual(max_char('123456789'), '9')

    def test_string_with_only_special_characters(self):
        self.assertEqual(max_char('!@#$%^&*()_+'), '*')
