import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):

    def test_single_character(self):
        self.assertEqual(ascii_value_string('a'), 97)
        self.assertEqual(ascii_value_string('A'), 65)
        self.assertEqual(ascii_value_string('1'), 49)
        self.assertEqual(ascii_value_string(' '), 32)

    def test_multiple_characters(self):
        self.assertEqual(ascii_value_string('ab'), 97)
        self.assertEqual(ascii_value_string('AB'), 65)
        self.assertEqual(ascii_value_string('12'), 49)
        self.assertEqual(ascii_value_string('  '), 32)

    def test_empty_string(self):
        self.assertIsNone(ascii_value_string(''))
