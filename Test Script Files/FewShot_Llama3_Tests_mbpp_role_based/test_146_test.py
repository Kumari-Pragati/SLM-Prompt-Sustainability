import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):
    def test_ascii_value_string_single_char(self):
        self.assertEqual(ascii_value_string('a'), ord('a'))

    def test_ascii_value_string_multiple_chars(self):
        self.assertEqual(ascii_value_string('abc'), ord('a'))
        self.assertEqual(ascii_value_string('abc'), ord('b'))
        self.assertEqual(ascii_value_string('abc'), ord('c'))

    def test_ascii_value_string_empty_string(self):
        with self.assertRaises(IndexError):
            ascii_value_string('')

    def test_ascii_value_string_non_string_input(self):
        with self.assertRaises(TypeError):
            ascii_value_string(123)
