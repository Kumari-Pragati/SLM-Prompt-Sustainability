import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(string_to_tuple("Hello World"), ('H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd'))

    def test_empty_string(self):
        self.assertEqual(string_to_tuple(""), ())

    def test_string_with_spaces(self):
        self.assertEqual(string_to_tuple("   "), ())

    def test_string_with_mixed_spaces_and_non_spaces(self):
        self.assertEqual(string_to_tuple("H e l l o   W o r l d"), ('H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd'))

    def test_string_with_special_characters(self):
        self.assertEqual(string_to_tuple("Hello@World"), ('H', 'e', 'l', 'l', 'o', '@', 'W', 'o', 'r', 'l', 'd'))
