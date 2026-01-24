import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):
    def test_found_substring(self):
        self.assertTrue(find_substring(["hello", "world", "python"], "world"))

    def test_not_found_substring(self):
        self.assertFalse(find_substring(["hello", "python"], "java"))

    def test_substring_in_multiple_strings(self):
        self.assertTrue(find_substring(["hello", "world", "python", "java"], "world"))

    def test_substring_in_single_string(self):
        self.assertTrue(find_substring(["hello"], "hello"))

    def test_substring_not_in_strings(self):
        self.assertFalse(find_substring(["hello", "python"], "ruby"))

    def test_empty_string(self):
        self.assertFalse(find_substring([""], "world"))

    def test_substring_in_empty_string(self):
        self.assertFalse(find_substring([""], ""))

    def test_substring_not_in_empty_string(self):
        self.assertFalse(find_substring([""], "world"))
