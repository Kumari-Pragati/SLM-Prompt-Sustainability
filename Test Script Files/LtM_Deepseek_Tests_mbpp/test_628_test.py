import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(replace_spaces("hello world"), "hello%20world")

    def test_string_with_multiple_spaces(self):
        self.assertEqual(replace_spaces("hello   world"), "hello%20%20%20world")

    def test_string_with_leading_trailing_spaces(self):
        self.assertEqual(replace_spaces(" hello world "), "%20hello%20world%20")

    def test_empty_string(self):
        self.assertEqual(replace_spaces(""), "")

    def test_string_with_max_length(self):
        long_string = "a" * 999
        self.assertEqual(replace_spaces(long_string), "a" * 999)

    def test_string_exceeding_max_length(self):
        long_string = "a" * 1001
        self.assertEqual(replace_spaces(long_string), -1)

    def test_string_with_special_characters(self):
        self.assertEqual(replace_spaces("hel!lo wor@ld"), "hel%20!lo%20wor%20@ld")
