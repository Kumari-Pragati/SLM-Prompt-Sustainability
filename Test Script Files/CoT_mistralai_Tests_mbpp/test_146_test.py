import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):
    def test_ascii_value_string_normal(self):
        self.assertEqual(ascii_value_string("abc"), 97 + 98 + 99)

    def test_ascii_value_string_empty_string(self):
        self.assertEqual(ascii_value_string(""), 0)

    def test_ascii_value_string_single_character(self):
        self.assertEqual(ascii_value_string("a"), 97)

    def test_ascii_value_string_special_characters(self):
        self.assertEqual(ascii_value_string("!@#$%^&*()_+-=[]{}|;:'\",.<>?/"), 33 + 64 + 65 + 66 + 67 + 68 + 69 + 70 + 71 + 72 + 73 + 74 + 75 + 76 + 77 + 78 + 79 + 80 + 81 + 82 + 83 + 84 + 85 + 86 + 87 + 88 + 89 + 90 + 91 + 92 + 93 + 94 + 95 + 96)

    def test_ascii_value_string_multi_byte_characters(self):
        self.assertEqual(ascii_value_string("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 65 + 66 + 67 + 68 + 69 + 70 + 71 + 72 + 73 + 74 + 75 + 76 + 77 + 78 + 79 + 80 + 81 + 82 + 83 + 84 + 85 + 86 + 87 + 88 + 89)

    def test_ascii_value_string_invalid_input(self):
        self.assertRaises(IndexError, ascii_value_string, "a" * 10001)
