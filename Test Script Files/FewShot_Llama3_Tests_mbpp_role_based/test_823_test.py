import unittest
from mbpp_823_code import check_substring

class TestCheckSubstring(unittest.TestCase):
    def test_string_starts_with_substring(self):
        self.assertEqual(check_substring("Hello, world!", "Hello"), "string starts with the given substring")

    def test_string_doesnt_start_with_substring(self):
        self.assertEqual(check_substring("Hello, world!", "Goodbye"), "string doesnt start with the given substring")

    def test_substring_not_in_string(self):
        self.assertEqual(check_substring("Hello, world!", "Goodbye, world!"), "entered string isnt a substring")

    def test_empty_string(self):
        self.assertEqual(check_substring("", "Hello"), "entered string isnt a substring")

    def test_empty_substring(self):
        self.assertEqual(check_substring("Hello, world!", ""), "entered string isnt a substring")

    def test_substring_at_end_of_string(self):
        self.assertEqual(check_substring("Hello, world!", "world"), "string doesnt start with the given substring")

    def test_substring_in_middle_of_string(self):
        self.assertEqual(check_substring("Hello, world!", "or"), "string doesnt start with the given substring")
