import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):

    def test_empty_string(self):
        """Test odd_values_string on an empty string"""
        self.assertEqual(odd_values_string(""), "")

    def test_single_character_string(self):
        """Test odd_values_string on a single character string"""
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(odd_values_string(char), char)

    def test_even_length_string(self):
        """Test odd_values_string on a string with even length"""
        for string in ["aa", "abcd", "xyzABC", "1234567890"]:
            self.assertEqual(odd_values_string(string), string[1::2])

    def test_odd_length_string(self):
        """Test odd_values_string on a string with odd length"""
        for string in ["a", "abcd", "xyzABC", "12345678901"]:
            self.assertEqual(odd_values_string(string), string)

    def test_string_with_only_odd_indexes(self):
        """Test odd_values_string on a string with only odd indexes"""
        self.assertEqual(odd_values_string("12345"), "135")

    def test_string_with_only_even_indexes(self):
        """Test odd_values_string on a string with only even indexes"""
        self.assertEqual(odd_values_string("2468"), "")

    def test_string_with_only_zero_index(self):
        """Test odd_values_string on a string with only zero index"""
        self.assertEqual(odd_values_string("a"), "")
