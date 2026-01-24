import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):

    def test_simple_substring(self):
        self.assertTrue(find_substring("hello world", "llo"))
        self.assertTrue(find_substring("Python is awesome", "thon"))

    def test_empty_strings(self):
        self.assertFalse(find_substring("", "test"))
        self.assertFalse(find_substring("test", ""))

    def test_single_char_substring(self):
        self.assertTrue(find_substring("a", "a"))
        self.assertFalse(find_substring("b", "a"))

    def test_case_sensitivity(self):
        self.assertTrue(find_substring("Python", "python"))
        self.assertFalse(find_substring("Python", "PythOn"))

    def test_multiple_substrings(self):
        self.assertTrue(find_substring("hello world", "llo world"))
        self.assertFalse(find_substring("hello world", "hello world1"))

    def test_substring_at_beginning(self):
        self.assertTrue(find_substring("hello world", "hello"))

    def test_substring_at_end(self):
        self.assertTrue(find_substring("hello world", "world"))

    def test_substring_in_middle(self):
        self.assertTrue(find_substring("hello world", "world"))

    def test_substring_in_middle_with_spaces(self):
        self.assertTrue(find_substring("hello world", " world"))

    def test_substring_with_special_characters(self):
        self.assertTrue(find_substring("Python@123", "@123"))
