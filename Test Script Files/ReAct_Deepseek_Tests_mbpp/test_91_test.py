import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(find_substring("Hello, world!", "world"))

    def test_edge_case_empty_string(self):
        self.assertFalse(find_substring("", "world"))

    def test_edge_case_sub_str_longer_than_str1(self):
        self.assertFalse(find_substring("Hello", "Hello, world!"))

    def test_edge_case_sub_str_not_in_str1(self):
        self.assertFalse(find_substring("Hello, world!", "universe"))

    def test_typical_case_multiple_occurrences(self):
        self.assertTrue(find_substring("Hello, world! world", "world"))

    def test_edge_case_sub_str_is_empty_string(self):
        self.assertTrue(find_substring("Hello, world!", ""))

    def test_edge_case_str1_is_empty_string(self):
        self.assertFalse(find_substring("", "world"))
