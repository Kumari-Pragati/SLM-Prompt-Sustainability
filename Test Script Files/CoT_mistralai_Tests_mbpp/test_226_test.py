import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(odd_values_string(""), "")

    def test_single_character(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(odd_values_string(char), char)

    def test_even_length_string(self):
        for string in ["aa", "abcd", "xyz", "123456"]:
            self.assertEqual(odd_values_string(string), string[1::2])

    def test_odd_length_string(self):
        for string in ["a", "abcd", "xyz", "12345"]:
            self.assertEqual(odd_values_string(string), string)

    def test_string_with_only_even_indexed_characters(self):
        self.assertEqual(odd_values_string("abcdef"), "c")

    def test_string_with_only_odd_indexed_characters(self):
        self.assertEqual(odd_values_string("abcdefg"), "abcdfg")

    def test_string_with_mixed_even_and_odd_indexed_characters(self):
        self.assertEqual(odd_values_string("abcdefghi"), "acghi")

    def test_string_with_special_characters(self):
        for string in ["!@#$%^&*()_+-=[]{}|;:'\",.<>?/":
            self.assertEqual(odd_values_string(string), string)

    def test_string_with_numbers(self):
        for string in ["1234567890", "12345678901234567890"]:
            self.assertEqual(odd_values_string(string), string)

    def test_string_with_mixed_characters_and_numbers(self):
        for string in ["abc123", "123abc", "12345678901234567890"]:
            self.assertEqual(odd_values_string(string), string)
