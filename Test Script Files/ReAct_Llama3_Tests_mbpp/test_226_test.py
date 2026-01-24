import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(odd_values_string(""), "")

    def test_single_character_string(self):
        self.assertEqual(odd_values_string("a"), "a")

    def test_even_length_string(self):
        self.assertEqual(odd_values_string("abc"), "a")

    def test_odd_length_string(self):
        self.assertEqual(odd_values_string("abcd"), "a")

    def test_long_string(self):
        self.assertEqual(odd_values_string("abcdefghijklmnopqrstuvwxyz"), "abc")

    def test_string_with_spaces(self):
        self.assertEqual(odd_values_string("hello world"), "hwo")

    def test_string_with_punctuation(self):
        self.assertEqual(odd_values_string("Hello, World!"), "HW")

    def test_string_with_numbers(self):
        self.assertEqual(odd_values_string("123abc456"), "123")

    def test_string_with_special_characters(self):
        self.assertEqual(odd_values_string("Hello!@#World"), "HW")
