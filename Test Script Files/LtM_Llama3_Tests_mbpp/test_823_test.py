import unittest
from mbpp_823_code import check_substring

class TestCheckSubstring(unittest.TestCase):
    def test_simple_valid(self):
        self.assertEqual(check_substring("hello world", "hello"), "string starts with the given substring")

    def test_simple_invalid(self):
        self.assertEqual(check_substring("hello world", "goodbye"), "string doesnt start with the given substring")

    def test_edge_empty_string(self):
        self.assertEqual(check_substring("", "hello"), "entered string isnt a substring")

    def test_edge_empty_sample(self):
        self.assertEqual(check_substring("hello world", ""), "entered string isnt a substring")

    def test_edge_empty_both(self):
        self.assertEqual(check_substring("", ""), "entered string isnt a substring")

    def test_edge_sample_longer_than_string(self):
        self.assertEqual(check_substring("hello", "worldhello"), "string doesnt start with the given substring")

    def test_edge_sample_same_as_string(self):
        self.assertEqual(check_substring("hello", "hello"), "string starts with the given substring")

    def test_edge_sample_longer_than_string_with_spaces(self):
        self.assertEqual(check_substring("hello world", "hello world"), "string starts with the given substring")
