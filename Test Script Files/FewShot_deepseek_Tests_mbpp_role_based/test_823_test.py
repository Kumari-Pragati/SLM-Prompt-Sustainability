import unittest
from mbpp_823_code import check_substring

class TestCheckSubstring(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(check_substring("hello world", "hello"), "string starts with the given substring")

    def test_edge_condition(self):
        self.assertEqual(check_substring("hello world", ""), "string starts with the given substring")

    def test_boundary_condition(self):
        self.assertEqual(check_substring("hello world", "h"), "string starts with the given substring")

    def test_invalid_input(self):
        self.assertEqual(check_substring("hello world", None), "entered string isnt a substring")

    def test_string_not_starting_with_substring(self):
        self.assertEqual(check_substring("world hello", "hello"), "string doesnt start with the given substring")

    def test_substring_not_in_string(self):
        self.assertEqual(check_substring("hello world", "hi"), "entered string isnt a substring")
