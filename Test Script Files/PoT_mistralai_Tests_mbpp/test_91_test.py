import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):

    def test_find_substring_typical_case(self):
        self.assertTrue(find_substring("Hello World", "World"))
        self.assertTrue(find_substring("Python is awesome", "awesome"))

    def test_find_substring_empty_string(self):
        self.assertFalse(find_substring("", "World"))

    def test_find_substring_empty_sub_string(self):
        self.assertFalse(find_substring("Hello World", ""))

    def test_find_substring_single_char_sub_string(self):
        self.assertTrue(find_substring("Hello World", "l"))
        self.assertTrue(find_substring("Hello World", "W"))

    def test_find_substring_case_sensitivity(self):
        self.assertFalse(find_substring("Hello World", "world"))

    def test_find_substring_multiple_sub_strings(self):
        self.assertTrue(find_substring("Hello World Hello", "Hello World"))
        self.assertTrue(find_substring("Hello World Hello", "Hello"))
        self.assertTrue(find_subscription("Hello World Hello", "World Hello"))
