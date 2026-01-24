import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):

    def test_empty_string(self):
        """Checks if the function correctly handles an empty string."""
        self.assertFalse(find_substring("", "sub_str"))

    def test_single_character_string(self):
        """Checks if the function correctly handles a single character string."""
        self.assertFalse(find_substring("a", "sub_str"))

    def test_substring_not_present(self):
        """Checks if the function correctly handles a string without the substring."""
        self.assertFalse(find_substring("hello world", "sub_str"))

    def test_substring_present_once(self):
        """Checks if the function correctly handles a string with the substring once."""
        self.assertTrue(find_substring("hello world", "world"))

    def test_substring_present_multiple_times(self):
        """Checks if the function correctly handles a string with the substring multiple times."""
        self.assertTrue(find_substring("hello world world", "world"))

    def test_substring_at_beginning(self):
        """Checks if the function correctly handles a string with the substring at the beginning."""
        self.assertTrue(find_substring("world hello", "world"))

    def test_substring_at_end(self):
        """Checks if the function correctly handles a string with the substring at the end."""
        self.assertTrue(find_substring("hello world", "world"))

    def test_substring_in_middle(self):
        """Checks if the function correctly handles a string with the substring in the middle."""
        self.assertTrue(find_substring("hello world hello", "world"))

    def test_substring_case_sensitivity(self):
        """Checks if the function is case-sensitive."""
        self.assertFalse(find_substring("Hello World", "world"))

    def test_empty_substring(self):
        """Checks if the function correctly handles an empty substring."""
        self.assertTrue(find_substring("hello", ""))
