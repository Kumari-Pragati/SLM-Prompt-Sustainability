import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(number_of_substrings('abc'), 6)

    def test_empty_string(self):
        self.assertEqual(number_of_substrings(''), 0)

    def test_single_character(self):
        self.assertEqual(number_of_substrings('a'), 1)

    def test_long_string(self):
        long_str = 'a' * 1000
        self.assertEqual(number_of_substrings(long_str), 500500)

    def test_special_characters(self):
        self.assertEqual(number_of_substrings('!@#$%^&*()'), 55)

    def test_whitespace(self):
        self.assertEqual(number_of_substrings(' '), 1)

    def test_repeated_characters(self):
        self.assertEqual(number_of_substrings('aaa'), 4)
