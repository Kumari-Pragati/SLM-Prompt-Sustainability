import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_replace_spaces_with_single_space(self):
        self.assertEqual(replace_spaces("hello world"), "h0l0l0w0r0l0d0")

    def test_replace_spaces_with_multiple_spaces(self):
        self.assertEqual(replace_spaces("hello   world"), "h0l0l0w0r0l0d0")

    def test_replace_spaces_with_no_spaces(self):
        self.assertEqual(replace_spaces("hello"), "hello")

    def test_replace_spaces_with_long_string(self):
        long_string = "a" * 998 + " " + "a" * 998
        self.assertLessEqual(len(replace_spaces(long_string)), 1000)

    def test_replace_spaces_with_empty_string(self):
        self.assertEqual(replace_spaces(""), "")

    def test_replace_spaces_with_string_longer_than_max(self):
        long_string = "a" * 1001 + " " + "a" * 1001
        self.assertEqual(replace_spaces(long_string), -1)
