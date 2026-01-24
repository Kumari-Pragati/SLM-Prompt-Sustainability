import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):

    def test_single_character_string(self):
        self.assertEqual(ascii_value_string('a'), ord('a'))
        self.assertEqual(ascii_value_string('A'), ord('A'))
        self.assertEqual(ascii_value_string('1'), ord('1'))
        self.assertEqual(ascii_value_string(' '), ord(' '))

    def test_empty_string(self):
        self.assertIsNone(ascii_value_string(''))

    def test_multi_character_string(self):
        self.assertEqual(ascii_value_string('abc'), ord('a'))
        self.assertEqual(ascii_value_string('ABC'), ord('A'))
        self.assertEqual(ascii_value_string('123'), ord('1'))
        self.assertEqual(ascii_value_string('ab1'), ord('a'))

    def test_special_characters(self):
        self.assertEqual(ascii_value_string('!@#'), ord('!'))
        self.assertEqual(ascii_value_string('?><'), ord('?'))
