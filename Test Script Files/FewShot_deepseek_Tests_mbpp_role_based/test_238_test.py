import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(number_of_substrings('abc'), 6)

    def test_empty_string(self):
        self.assertEqual(number_of_substrings(''), 0)

    def test_single_character_string(self):
        self.assertEqual(number_of_substrings('a'), 1)

    def test_long_string(self):
        self.assertEqual(number_of_substrings('abcdefghijklmnopqrstuvwxyz'), 285)

    def test_string_with_special_characters(self):
        self.assertEqual(number_of_substrings('abc@123'), 9)
