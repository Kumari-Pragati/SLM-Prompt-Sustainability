import unittest
from mbpp_813_code import string_length

class TestStringLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(string_length("hello"), 5)

    def test_empty_string(self):
        self.assertEqual(string_length(""), 0)

    def test_single_character(self):
        self.assertEqual(string_length("a"), 1)

    def test_long_string(self):
        self.assertEqual(string_length("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_multi_line_string(self):
        multi_line_str = """
        This is a multi-line string
        with multiple lines
        """
        self.assertEqual(string_length(multi_line_str), 46)

    def test_whitespace_only_string(self):
        self.assertEqual(string_length("   "), 3)

    def test_unicode_string(self):
        unicode_str = "\u00E9l\u0303h\u00E9ll\u00F3"
        self.assertEqual(string_length(unicode_str), 9)
