import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):
    def test_single_character_string(self):
        self.assertEqual(max_char('a'), 'a')

    def test_multiple_characters_string(self):
        self.assertEqual(max_char('abcdefg'), 'g')

    def test_empty_string(self):
        self.assertEqual(max_char(''), '')

    def test_string_with_duplicate_characters(self):
        self.assertEqual(max_char('aaabbbccc'), 'c')

    def test_string_with_only_spaces(self):
        self.assertEqual(max_char('   '), ' ')

    def test_string_with_special_characters(self):
        self.assertEqual(max_char('!@#$%^&*()_+-=[]{}|;:'\''"<>,.?/'), ';')
