import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):
    def test_found_substring(self):
        self.assertTrue(find_substring(["hello world", "python is fun"], "world"))

    def test_not_found_substring(self):
        self.assertFalse(find_substring(["hello world", "python is fun"], "java"))

    def test_empty_string(self):
        self.assertFalse(find_substring([""], "world"))

    def test_empty_list(self):
        self.assertFalse(find_substring([], "world"))

    def test_single_element_list(self):
        self.assertTrue(find_substring(["hello world"], "world"))

    def test_substring_in_all_strings(self):
        self.assertTrue(find_substring(["hello world", "world is fun"], "world"))

    def test_substring_in_none_of_strings(self):
        self.assertFalse(find_substring(["hello world", "python is fun"], "java"))
