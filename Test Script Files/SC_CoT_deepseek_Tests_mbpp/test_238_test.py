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
        self.assertEqual(number_of_substrings('abcdefghijklmnopqrstuvwxyz'), 285)

    def test_special_characters(self):
        self.assertEqual(number_of_substrings('!@#$%^&*()'), 55)

    def test_numeric_string(self):
        self.assertEqual(number_of_substrings('123456'), 21)

    def test_string_with_spaces(self):
        self.assertEqual(number_of_substrings('Hello World'), 11)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            number_of_substrings(12345)
