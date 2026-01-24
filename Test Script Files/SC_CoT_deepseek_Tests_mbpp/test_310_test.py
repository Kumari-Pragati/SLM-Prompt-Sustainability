import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(string_to_tuple("hello world"), ('h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd'))

    def test_empty_string(self):
        self.assertEqual(string_to_tuple(""), ())

    def test_string_with_spaces(self):
        self.assertEqual(string_to_tuple("   "), ())

    def test_string_with_special_characters(self):
        self.assertEqual(string_to_tuple("!@#$%^&*()"), tuple("!@#$%^&*()"))

    def test_string_with_numbers(self):
        self.assertEqual(string_to_tuple("1234567890"), tuple("1234567890"))

    def test_string_with_mixed_case(self):
        self.assertEqual(string_to_tuple("HeLlO WoRlD"), ('H', 'e', 'L', 'l', 'O', 'W', 'O', 'R', 'L', 'D'))

    def test_string_with_mixed_characters(self):
        self.assertEqual(string_to_tuple("h1e2l3l4o5w6o7r8l9d0"), ('h', '1', 'e', '2', 'l', '3', 'l', '4', 'o', '5', 'w', '6', 'o', '7', 'r', '8', 'l', '9', 'd', '0'))
