import unittest
from mbpp_823_code import check_substring

class TestCheckSubstring(unittest.TestCase):

    def test_substring_present_and_starts_with(self):
        self.assertEqual(check_substring("Hello World", "Hello"), "string starts with the given substring")

    def test_substring_present_but_not_starts_with(self):
        self.assertEqual(check_substring("World Hello", "Hello"), "string doesnt start with the given substring")

    def test_substring_not_present(self):
        self.assertEqual(check_substring("Hello World", "Goodbye"), "entered string isnt a substring")

    def test_empty_string(self):
        self.assertEqual(check_substring("", "Hello"), "entered string isnt a substring")

    def test_sample_is_empty(self):
        self.assertEqual(check_substring("Hello World", ""), "entered string isnt a substring")
