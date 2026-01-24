import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(get_max_occuring_char(''), '')

    def test_single_character(self):
        self.assertEqual(get_max_occuring_char('a'), 'a')

    def test_multiple_characters(self):
        self.assertEqual(get_max_occuring_char('aaabbbccc'), 'c')

    def test_case_sensitivity(self):
        self.assertEqual(get_max_occuring_char('ABCabc'), 'c')

    def test_special_characters(self):
        self.assertEqual(get_max_occuring_char('!@#$%^&*()_+-=[]{}|;:,.<>?'), ' ')

    def test_unicode_string(self):
        self.assertEqual(get_max_occuring_char('🐶🐺🐺🐺🐶🐺'), '🐺')
