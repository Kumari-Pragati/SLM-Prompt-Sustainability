import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(ascii_value('a'), 97)

    def test_uppercase(self):
        self.assertEqual(ascii_value('A'), 65)

    def test_digit(self):
        self.assertEqual(ascii_value('0'), 48)

    def test_special_char(self):
        self.assertEqual(ascii_value('!'), 33)

    def test_empty_string(self):
        with self.assertRaises(TypeError):
            ascii_value('')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            ascii_value(123)
