import unittest
from mbpp_823_code import check_substring

class TestCheckSubstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_substring("Hello, World!", "World"), "string starts with the given substring")

    def test_edge_case_start(self):
        self.assertEqual(check_substring("World, Hello!", "World"), "string starts with the given substring")

    def test_edge_case_end(self):
        self.assertEqual(check_substring("Hello, World!", "Hello"), "string starts with the given substring")

    def test_edge_case_middle(self):
        self.assertEqual(check_substring("Hello, World!", "o"), "string doesnt start with the given substring")

    def test_edge_case_empty(self):
        self.assertEqual(check_substring("", "World"), "entered string isnt a substring")

    def test_edge_case_non_string(self):
        self.assertEqual(check_substring(123, "World"), "entered string isnt a substring")

    def test_edge_case_non_substring(self):
        self.assertEqual(check_substring("Hello, World!", "Universe"), "string doesnt start with the given substring")

    def test_edge_case_substring_not_found(self):
        self.assertEqual(check_substring("Hello, World!", "Moon"), "string doesnt start with the given substring")
