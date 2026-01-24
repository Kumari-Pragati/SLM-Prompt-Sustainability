import unittest
from mbpp_823_code import check_substring

class TestCheckSubstring(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(check_substring("hello world", "hello"), "string starts with the given substring")

    def test_edge_case_empty_string(self):
        self.assertEqual(check_substring("", "hello"), "entered string isnt a substring")

    def test_edge_case_empty_substring(self):
        self.assertEqual(check_substring("hello world", ""), "string starts with the given substring")

    def test_boundary_case_max_string(self):
        max_string = 'a' * 10000
        self.assertEqual(check_substring(max_string, "a"), "string starts with the given substring")

    def test_boundary_case_max_substring(self):
        max_substring = 'a' * 5000
        self.assertEqual(check_substring("a" * 10000, max_substring), "string starts with the given substring")

    def test_complex_case_no_match(self):
        self.assertEqual(check_substring("hello world", "world!"), "string doesnt start with the given substring")

    def test_complex_case_match_at_end(self):
        self.assertEqual(check_substring("hello world", "world"), "string starts with the given substring")
