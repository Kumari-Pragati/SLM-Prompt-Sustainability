import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):
    def test_find_substring_present(self):
        self.assertTrue(find_substring("Hello World", "World"))
        self.assertTrue(find_substring("Python is awesome", "awesome"))
        self.assertTrue(find_substring("abcabc", "abc"))

    def test_find_substring_absent(self):
        self.assertFalse(find_substring("Hello World", "Hello"))
        self.assertFalse(find_substring("Python is awesome", "Python2"))
        self.assertFalse(find_substring("abcabc", "xyz"))

    def test_find_substring_empty_strings(self):
        self.assertFalse(find_substring("", "World"))
        self.assertFalse(find_substring("World", ""))

    def test_find_substring_single_char(self):
        self.assertTrue(find_substring("a", "a"))
        self.assertFalse(find_substring("b", "a"))

    def test_find_substring_case_sensitivity(self):
        self.assertTrue(find_substring("Hello World", "world"))
        self.assertFalse(find_substring("Hello World", "World1"))

    def test_find_substring_multiple_substrings(self):
        self.assertTrue(find_substring("Hello World World", "World"))
        self.assertTrue(find_substring("Hello World World", "Hello"))
