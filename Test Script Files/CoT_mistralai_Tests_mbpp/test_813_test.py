import unittest
from mbpp_813_code import string_length

class TestStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(string_length(''), 0)

    def test_single_character_string(self):
        self.assertEqual(string_length('a'), 1)

    def test_multiple_characters_string(self):
        self.assertEqual(string_length('abc'), 3)

    def test_string_with_spaces(self):
        self.assertEqual(string_length('hello world'), 11)

    def test_long_string(self):
        long_string = 'x' * 100
        self.assertEqual(len(long_string), string_length(long_string))

    def test_string_with_special_characters(self):
        self.assertEqual(string_length('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), 47)

    def test_string_with_unicode(self):
        self.assertEqual(string_length('\u4e2d\u6587'), 2)

    def test_string_with_empty_spaces(self):
        self.assertEqual(string_length('   '), 3)

    def test_string_with_only_whitespace(self):
        self.assertEqual(string_length('\n\r\t'), 3)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            string_length(None)

    def test_invalid_input_int(self):
        with self.assertRaises(TypeError):
            string_length(123)
