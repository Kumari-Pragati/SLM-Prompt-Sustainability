import unittest
from mbpp_823_code import check_substring

class TestCheckSubstring(unittest.TestCase):

    def test_substring_at_start(self):
        self.assertEqual(check_substring("hello world", "hello"), "string starts with the given substring")

    def test_substring_not_at_start(self):
        self.assertEqual(check_substring("hello world", "world"), "string doesnt start with the given substring")

    def test_substring_not_present(self):
        self.assertEqual(check_substring("hello world", "hi"), "entered string isnt a substring")

    def test_empty_string(self):
        self.assertEqual(check_substring("", "hello"), "entered string isnt a substring")

    def test_empty_substring(self):
        self.assertEqual(check_substring("hello world", ""), "string starts with the given substring")

    def test_substring_equal_to_string(self):
        self.assertEqual(check_substring("hello world", "hello world"), "string starts with the given substring")

    def test_whitespace_only_substring(self):
        self.assertEqual(check_substring("hello world", " "), "string starts with the given substring")

    def test_special_characters_in_substring(self):
        self.assertEqual(check_substring("hello world", "@world"), "string doesnt start with the given substring")
