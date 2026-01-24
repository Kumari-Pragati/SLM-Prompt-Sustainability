import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):

    def test_find_substring_true(self):
        self.assertTrue(find_substring(["hello", "world", "python"], "world"))

    def test_find_substring_false(self):
        self.assertFalse(find_substring(["hello", "world", "python"], "java"))

    def test_find_substring_empty_list(self):
        self.assertFalse(find_substring([], "world"))

    def test_find_substring_empty_substring(self):
        self.assertFalse(find_substring(["hello", "world", "python"], ""))

    def test_find_substring_substring_in_all_strings(self):
        self.assertTrue(find_substring(["hello", "world", "python"], "hello"))

    def test_find_substring_substring_in_none_strings(self):
        self.assertFalse(find_substring(["hello", "python"], "java"))
