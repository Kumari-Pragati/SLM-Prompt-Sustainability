import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):

    def test_single_character_string(self):
        self.assertEqual(ascii_value_string('a'), ord('a'))
        self.assertEqual(ascii_value_string('A'), ord('A'))
        self.assertEqual(ascii_value_string('1'), ord('1'))

    def test_multiple_character_string(self):
        self.assertEqual(ascii_value_string('abc'), ord('a'))
        self.assertEqual(ascii_value_string('ABC'), ord('A'))
        self.assertEqual(ascii_value_string('123'), ord('1'))

    def test_empty_string(self):
        self.assertIsNone(ascii_value_string(''))

    def test_special_characters(self):
        self.assertEqual(ascii_value_string('!@#'), ord('!'))
        self.assertEqual(ascii_value_string('^&*'), ord('^'))

    def test_whitespace(self):
        self.assertEqual(ascii_value_string(' '), ord(' '))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            ascii_value_string(123)
        with self.assertRaises(TypeError):
            ascii_value_string(None)
