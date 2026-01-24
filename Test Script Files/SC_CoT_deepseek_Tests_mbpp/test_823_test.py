import unittest
from mbpp_823_code import check_substring

class TestCheckSubstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_substring("hello world", "hello"), "string starts with the given substring")

    def test_edge_case(self):
        self.assertEqual(check_substring("hello world", ""), "string starts with the given substring")

    def test_corner_case(self):
        self.assertEqual(check_substring("hello world", "world"), "string doesnt start with the given substring")

    def test_invalid_input(self):
        self.assertEqual(check_substring("hello world", 123), "entered string isnt a substring")

    def test_no_substring(self):
        self.assertEqual(check_substring("hello world", "hi"), "entered string isnt a substring")
