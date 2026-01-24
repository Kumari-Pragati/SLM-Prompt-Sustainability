import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(find_substring("Hello, world!", "world"))

    def test_edge_case_empty_string(self):
        self.assertFalse(find_substring("", "world"))

    def test_boundary_case_sub_str_longer_than_str1(self):
        self.assertFalse(find_substring("Hello", "Hello, world!"))

    def test_boundary_case_sub_str_equal_to_str1(self):
        self.assertTrue(find_substring("Hello, world!", "Hello, world!"))

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            find_substring(None, "world")

    def test_invalid_input_sub_str_none(self):
        with self.assertRaises(TypeError):
            find_substring("Hello, world!", None)
