import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):
    def test_find_substring_in_string(self):
        self.assertTrue(find_substring("Hello World", "World"))

    def test_find_substring_not_in_string(self):
        self.assertFalse(find_substring("Hello World", "Hello"))

    def test_find_substring_empty_string(self):
        self.assertFalse(find_substring("", "World"))

    def test_find_substring_single_char_string(self):
        self.assertFalse(find_substring("a", "b"))

    def test_find_substring_sub_string_empty(self):
        self.assertTrue(find_substring("Hello World", ""))
