import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_allowed_specific_char(''))

    def test_alphabets(self):
        self.assertTrue(is_allowed_specific_char('abc'))
        self.assertTrue(is_allowed_specific_char('ABC'))
        self.assertTrue(is_allowed_specific_char('123'))
        self.assertTrue(is_allowed_specific_char('._'))

    def test_mixed_case(self):
        self.assertTrue(is_allowed_specific_char('AbC123._'))

    def test_long_string(self):
        long_string = 'a' * 100 + '.' * 10 + '0' * 100
        self.assertTrue(is_allowed_specific_char(long_string))

    def test_single_special_char(self):
        for char in ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '+', ',', '.', ';', ':', '"', '\'', '\\', '|', '[', ']', '{', '}', '^', '_', '~', '`', '>', '<', '?', '/':
            self.assertFalse(is_allowed_specific_char(char))

    def test_multiple_special_chars(self):
        forbidden_string = '!@#$%&*()-+,.:;"'\"\\|[]{}^_~`><?/'
        self.assertFalse(is_allowed_specific_char(forbidden_string))

    def test_empty_list(self):
        self.assertRaises(ValueError, is_allowed_specific_char, [])

    def test_single_element_list(self):
        for char in ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '+', ',', '.', ';', ':', '"', '\'', '\\', '|', '[', ']', '{', '}', '^', '_', '~', '`', '>', '<', '?', '/']:
            self.assertFalse(is_allowed_specific_char([char]))

    def test_list_with_allowed_chars(self):
        self.assertTrue(is_allowed_specific_char(['a', 'b', 'c', '.', '_']))
