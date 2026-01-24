import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):

    def test_ascii_value_normal_case(self):
        self.assertEqual(ascii_value('a'), 97)

    def test_ascii_value_uppercase_case(self):
        self.assertEqual(ascii_value('B'), 66)

    def test_ascii_value_digit_case(self):
        self.assertEqual(ascii_value('5'), 53)

    def test_ascii_value_special_char_case(self):
        self.assertEqual(ascii_value('@'), 64)

    def test_ascii_value_empty_string_case(self):
        self.assertEqual(ascii_value(''), 0)

    def test_ascii_value_non_string_case(self):
        with self.assertRaises(TypeError):
            ascii_value(123)
