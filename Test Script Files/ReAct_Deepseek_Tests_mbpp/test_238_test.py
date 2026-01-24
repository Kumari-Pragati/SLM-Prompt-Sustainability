import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(number_of_substrings('abc'), 6)
        self.assertEqual(number_of_substrings('123'), 6)
        self.assertEqual(number_of_substrings('a1b2c3'), 15)

    def test_empty_string(self):
        self.assertEqual(number_of_substrings(''), 0)

    def test_single_character(self):
        self.assertEqual(number_of_substrings('a'), 1)

    def test_long_string(self):
        long_string = 'a' * 1000
        expected_substrings = int(len(long_string) * (len(long_string) + 1) / 2)
        self.assertEqual(number_of_substrings(long_string), expected_substrings)
