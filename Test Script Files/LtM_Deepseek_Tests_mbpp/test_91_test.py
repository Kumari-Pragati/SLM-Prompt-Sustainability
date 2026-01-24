import unittest
from mbpp_91_code import find_substring

class TestFindSubstring(unittest.TestCase):

    def test_simple_case(self):
        self.assertTrue(find_substring("Hello World", "World"))

    def test_edge_case_empty_string(self):
        self.assertFalse(find_substring("", "World"))

    def test_edge_case_empty_substring(self):
        self.assertTrue(find_substring("Hello World", ""))

    def test_boundary_case_substring_longer_than_string(self):
        self.assertFalse(find_substring("Hello", "Hello World"))

    def test_complex_case_substring_not_present(self):
        self.assertFalse(find_substring("Hello World", "Earth"))

    def test_complex_case_substring_present_multiple_times(self):
        self.assertTrue(find_substring("Hello World, World", "World"))
