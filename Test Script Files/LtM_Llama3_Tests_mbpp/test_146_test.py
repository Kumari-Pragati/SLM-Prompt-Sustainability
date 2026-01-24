import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):
    def test_simple_ascii_values(self):
        self.assertEqual(ascii_value_string("a"), 97)
        self.assertEqual(ascii_value_string("b"), 98)
        self.assertEqual(ascii_value_string("c"), 99)

    def test_edge_cases(self):
        self.assertEqual(ascii_value_string(""), None)
        self.assertEqual(ascii_value_string(" "), 32)
        self.assertEqual(ascii_value_string("a"), 97)

    def test_ascii_values_at_end(self):
        self.assertEqual(ascii_value_string("abc"), 99)
        self.assertEqual(ascii_value_string("xyz"), 121)

    def test_ascii_values_at_start(self):
        self.assertEqual(ascii_value_string("abc"), 97)
        self.assertEqual(ascii_value_string("xyz"), 120)

    def test_non_ascii_characters(self):
        self.assertEqual(ascii_value_string("ä"), 228)
        self.assertEqual(ascii_value_string("ö"), 246)
