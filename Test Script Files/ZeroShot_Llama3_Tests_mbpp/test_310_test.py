import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):

    def test_string_to_tuple(self):
        self.assertEqual(string_to_tuple("Hello World"), ("Hello", "World"))
        self.assertEqual(string_to_tuple("   "), ())
        self.assertEqual(string_to_tuple("Hello"), ("Hello",))
        self.assertEqual(string_to_tuple(""), ())
        self.assertEqual(string_to_tuple("   Hello   "), ("Hello",))
        self.assertEqual(string_to_tuple("Hello, World!"), ("Hello", "World"))
        self.assertEqual(string_to_tuple("   Hello,   World!   "), ("Hello", "World"))

    def test_string_to_tuple_with_punctuation(self):
        self.assertEqual(string_to_tuple("Hello, World!"), ("Hello", "World"))
        self.assertEqual(string_to_tuple("Hello, World!   "), ("Hello", "World"))
        self.assertEqual(string_to_tuple("   Hello,   World!   "), ("Hello", "World"))

    def test_string_to_tuple_with_numbers(self):
        self.assertEqual(string_to_tuple("Hello 123 World"), ("Hello", "123", "World"))
        self.assertEqual(string_to_tuple("   Hello 123 World   "), ("Hello", "123", "World"))
        self.assertEqual(string_to_tuple("Hello 123, World!"), ("Hello", "123", "World"))
        self.assertEqual(string_to_tuple("   Hello 123,   World!   "), ("Hello", "123", "World"))
