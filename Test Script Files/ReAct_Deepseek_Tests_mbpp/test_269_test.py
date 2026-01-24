import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):

    def test_ascii_value_typical_case(self):
        self.assertEqual(ascii_value('a'), 97)

    def test_ascii_value_upper_case(self):
        self.assertEqual(ascii_value('A'), 65)

    def test_ascii_value_numeric_character(self):
        self.assertEqual(ascii_value('0'), 48)

    def test_ascii_value_special_character(self):
        self.assertEqual(ascii_value('@'), 64)

    def test_ascii_value_space_character(self):
        self.assertEqual(ascii_value(' '), 32)

    def test_ascii_value_error_case(self):
        with self.assertRaises(TypeError):
            ascii_value(123)
