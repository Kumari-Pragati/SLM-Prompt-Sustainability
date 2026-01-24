import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_empty_string(self):
        """Test if an empty string returns an empty string"""
        self.assertEqual(remove_even(""), "")

    def test_single_character_string(self):
        """Test if a single character string returns the same character"""
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(remove_even(char), char)

    def test_even_length_string(self):
        """Test if a string with even length returns an empty string"""
        for even_str in ["aa", "abcdef", "12345678"]:
            self.assertEqual(remove_even(even_str), "")

    def test_odd_length_string(self):
        """Test if a string with odd length returns the original string"""
        for odd_str in ["a", "abcde", "12345"]:
            self.assertEqual(remove_even(odd_str), odd_str)

    def test_string_with_spaces(self):
        """Test if a string with spaces behaves correctly"""
        for space_str in ["hello world", "  foo  bar  ", "123 456 789"]:
            self.assertEqual(remove_even(space_str), space_str.replace(" ", ""))

    def test_string_with_special_characters(self):
        """Test if a string with special characters behaves correctly"""
        for special_str in ["!@#$%^&*()_+-=", "abc!def", "123_456"]:
            self.assertEqual(remove_even(special_str), special_str.replace(" ", ""))
