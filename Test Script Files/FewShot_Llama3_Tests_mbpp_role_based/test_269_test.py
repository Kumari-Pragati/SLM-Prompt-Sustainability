import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):
    def test_ascii_value_lowercase(self):
        self.assertEqual(ascii_value('a'), 97)

    def test_ascii_value_uppercase(self):
        self.assertEqual(ascii_value('A'), 65)

    def test_ascii_value_digit(self):
        self.assertEqual(ascii_value('0'), 48)

    def test_ascii_value_special_character(self):
        self.assertEqual(ascii_value('!'), 33)

    def test_ascii_value_empty_string(self):
        with self.assertRaises(TypeError):
            ascii_value('')

    def test_ascii_value_non_string_input(self):
        with self.assertRaises(TypeError):
            ascii_value(123)
