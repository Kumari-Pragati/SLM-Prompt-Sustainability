import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):
    def test_single_character_string(self):
        self.assertEqual(ascii_value_string('A'), 65)

    def test_multi_character_string(self):
        self.assertEqual(ascii_value_string('Hello'), 72 + 101 + 108 + 108 + 111)

    def test_empty_string(self):
        self.assertEqual(ascii_value_string(''), 0)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            ascii_value_string(123)
