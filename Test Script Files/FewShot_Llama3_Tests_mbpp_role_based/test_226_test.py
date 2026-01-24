import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(odd_values_string(""), "")

    def test_single_character_string(self):
        self.assertEqual(odd_values_string("a"), "a")

    def test_even_length_string(self):
        self.assertEqual(odd_values_string("abcdef"), "abc")

    def test_odd_length_string(self):
        self.assertEqual(odd_values_string("abcdefg"), "abc")

    def test_string_with_spaces(self):
        self.assertEqual(odd_values_string("hello world"), "hlo")

    def test_string_with_punctuation(self):
        self.assertEqual(odd_values_string("Hello, World!"), "Hlo")

    def test_string_with_numbers(self):
        self.assertEqual(odd_values_string("123456"), "123")
