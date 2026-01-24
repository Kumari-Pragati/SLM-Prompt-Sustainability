import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(number_of_substrings(""), 0)

    def test_single_character_string(self):
        self.assertEqual(number_of_substrings("a"), 1)

    def test_short_string(self):
        self.assertEqual(number_of_substrings("abc"), 4)

    def test_long_string(self):
        long_string = "x" * 100
        self.assertEqual(number_of_substrings(long_string), 50050)

    def test_string_with_spaces(self):
        self.assertEqual(number_of_substrings("hello world"), 12)
