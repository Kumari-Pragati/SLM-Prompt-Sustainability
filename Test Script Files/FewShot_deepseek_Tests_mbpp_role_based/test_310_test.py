import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(string_to_tuple("Hello World"), ('H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd'))

    def test_empty_string(self):
        self.assertEqual(string_to_tuple(""), ())

    def test_string_with_spaces(self):
        self.assertEqual(string_to_tuple("   "), ())

    def test_string_with_special_characters(self):
        self.assertEqual(string_to_tuple("!@#$%^&*()"), ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')'))

    def test_string_with_numbers(self):
        self.assertEqual(string_to_tuple("1234567890"), ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))

    def test_string_with_mixed_characters(self):
        self.assertEqual(string_to_tuple("123 Hello World!@#"), ('1', '2', '3', 'H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd', '!', '@', '#'))
