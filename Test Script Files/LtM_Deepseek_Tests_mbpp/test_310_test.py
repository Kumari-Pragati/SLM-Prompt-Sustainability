import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(string_to_tuple("hello"), ('h', 'e', 'l', 'l', 'o'))

    def test_empty_string(self):
        self.assertEqual(string_to_tuple(""), ())

    def test_string_with_spaces(self):
        self.assertEqual(string_to_tuple("hello world"), ('h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd'))

    def test_string_with_special_characters(self):
        self.assertEqual(string_to_tuple("hello@world"), ('h', 'e', 'l', 'l', 'o', '@', 'w', 'o', 'r', 'l', 'd'))

    def test_string_with_numbers(self):
        self.assertEqual(string_to_tuple("12345"), ('1', '2', '3', '4', '5'))

    def test_string_with_mixed_characters(self):
        self.assertEqual(string_to_tuple("123hello456world789"), ('1', '2', '3', 'h', 'e', 'l', 'l', 'o', '4', '5', '6', 'w', 'o', 'r', 'l', 'd', '7', '8', '9'))
