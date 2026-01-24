import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(find_substring(["hello", "world"], "world"))

    def test_sub_str_not_in_str1(self):
        self.assertFalse(find_substring(["hello", "world"], "earth"))

    def test_empty_sub_str(self):
        self.assertTrue(find_substring(["hello", "world"], ""))

    def test_empty_str1(self):
        self.assertFalse(find_substring([], "world"))

    def test_sub_str_is_none(self):
        with self.assertRaises(TypeError):
            find_substring(["hello", "world"], None)

    def test_str1_is_none(self):
        with self.assertRaises(TypeError):
            find_substring(None, "world")

    def test_str1_contains_none(self):
        with self.assertRaises(TypeError):
            find_substring(["hello", None], "world")
