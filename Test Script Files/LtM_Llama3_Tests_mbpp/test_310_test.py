import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(string_to_tuple(""), ())

    def test_single_char(self):
        self.assertEqual(string_to_tuple("a"), ('a',))

    def test_multiple_chars(self):
        self.assertEqual(string_to_tuple("hello"), ('hello',))

    def test_spaces(self):
        self.assertEqual(string_to_tuple("   "), ())

    def test_mixed_chars(self):
        self.assertEqual(string_toTuple("hello world"), ('hello', 'world'))

    def test_non_ascii_chars(self):
        self.assertEqual(string_to_tuple("hëllo"), ('hëllo',))

    def test_empty_string_with_spaces(self):
        self.assertEqual(string_to_tuple("   "), ())

    def test_string_with_leading_spaces(self):
        self.assertEqual(string_to_tuple("   hello"), ('hello',))

    def test_string_with_trailing_spaces(self):
        self.assertEqual(string_to_tuple("hello   "), ('hello',))

    def test_string_with_mixed_spaces(self):
        self.assertEqual(string_to_tuple("hello   world"), ('hello', 'world'))

    def test_string_with_non_ascii_chars_and_spaces(self):
        self.assertEqual(string_to_tuple("hëllo   world"), ('hëllo', 'world'))
