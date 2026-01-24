import unittest
from mbpp_823_code import check_substring

class TestCheckSubstring(unittest.TestCase):

    def test_substring_at_start(self):
        self.assertEqual(check_substring("HelloWorld", "Hello"), "string starts with the given substring")

    def test_substring_not_at_start(self):
        self.assertEqual(check_substring("WorldHello", "Hello"), "string doesnt start with the given substring")

    def test_substring_not_present(self):
        self.assertEqual(check_substring("HelloWorld", "Hi"), "entered string isnt a substring")

    def test_empty_string(self):
        self.assertEqual(check_substring("", "Hello"), "entered string isnt a substring")

    def test_substring_equal_to_string(self):
        self.assertEqual(check_substring("Hello", "Hello"), "string starts with the given substring")

    def test_empty_substring(self):
        self.assertEqual(check_substring("Hello", ""), "string starts with the given substring")
