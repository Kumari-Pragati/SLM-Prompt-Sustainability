import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_extra_char(''), '')

    def test_single_char(self):
        self.assertEqual(remove_extra_char('a'), 'a')
        self.assertEqual(remove_extra_char('A'), 'A')
        self.assertEqual(remove_extra_char('0'), '0')

    def test_multiple_chars(self):
        self.assertEqual(remove_extra_char('ab'), 'ab')
        self.assertEqual(remove_extra_char('AB'), 'AB')
        self.assertEqual(remove_extra_char('01'), '01')

    def test_whitespace(self):
        self.assertEqual(remove_extra_char(' a '), 'a')
        self.assertEqual(remove_extra_char('\t\n\r '), '')

    def test_special_characters(self):
        self.assertEqual(remove_extra_char('!@#$%^&*()_+-=[]{}|;:,.<>?'), '!@#$%^&*()_+-=[]{}|;:,.<>')

    def test_numbers_with_underscores(self):
        self.assertEqual(remove_extra_char('1_2_3'), '123')
        self.assertEqual(remove_extra_char('1_2_3_4_5_6'), '123456')

    def test_numbers_with_special_characters(self):
        self.assertEqual(remove_extra_char('1!2@3#4$5%6^7&8*9(0)'), '123456')

    def test_mixed_case_string(self):
        self.assertEqual(remove_extra_char('AbCdEfGhIjKlMnOpQrStUvWxYz'), 'abcdefghijklmnopqrstuvwxyz')

    def test_long_string(self):
        long_string = 'a' * 100
        self.assertEqual(remove_extra_char(long_string), long_string)

    def test_empty_list_input(self):
        with self.assertRaises(TypeError):
            remove_extra_char([])

    def test_none_input(self):
        with self.assertRaises(TypeError):
            remove_extra_char(None)
