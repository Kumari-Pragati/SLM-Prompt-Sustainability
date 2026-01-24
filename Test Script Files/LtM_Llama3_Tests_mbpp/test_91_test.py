import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):
    def test_true(self):
        self.assertTrue(find_substring(["hello", "world"], "world"))

    def test_false(self):
        self.assertFalse(find_substring(["hello", "world"], "abc"))

    def test_empty_input(self):
        self.assertFalse(find_substring([], "world"))

    def test_substring_empty(self):
        self.assertFalse(find_substring(["hello", "world"], ""))

    def test_substring_in_multiple_strings(self):
        self.assertTrue(find_substring(["hello", "world", "python"], "world"))

    def test_substring_in_single_string(self):
        self.assertTrue(find_substring(["hello"], "hello"))

    def test_substring_not_found(self):
        self.assertFalse(find_substring(["hello", "world"], "python"))
