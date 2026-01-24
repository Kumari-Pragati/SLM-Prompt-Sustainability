import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(ascii_value_string("abc"), 97 + 98 + 99)

    def test_edge_case_empty_string(self):
        self.assertEqual(ascii_value_string(""), 0)

    def test_edge_case_single_char(self):
        self.assertEqual(ascii_value_string("a"), 97)

    def test_edge_case_long_string(self):
        self.assertEqual(ascii_value_string("abcdefghijklmnopqrstuvwxyz"), 97 * 26 + 122)

    def test_edge_case_uppercase_string(self):
        self.assertEqual(ascii_value_string("ABC"), 65 * 3)

    def test_edge_case_special_characters(self):
        self.assertEqual(ascii_value_string("!@#$%^&*()_+-=[]{}|;:'\",.<>?/"), 33 + 64 + 65 + 66 + 67 + 68 + 69 + 70 + 71 + 72 + 73 + 74 + 75 + 76 + 77 + 78 + 79 + 80 + 81 + 82 + 83 + 84 + 85 + 86 + 87 + 88 + 89 + 90 + 91 + 92 + 93 + 94 + 95 + 96)
