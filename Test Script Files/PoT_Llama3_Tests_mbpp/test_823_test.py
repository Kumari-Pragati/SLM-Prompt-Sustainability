import unittest
from mbpp_823_code import check_substring

class TestCheckSubstring(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(check_substring("hello world", "world"), "string starts with the given substring")

    def test_edge_case_start(self):
        self.assertEqual(check_substring("world hello", "world"), "string starts with the given substring")

    def test_edge_case_end(self):
        self.assertEqual(check_substring("hello world", "world"), "string starts with the given substring")

    def test_edge_case_middle(self):
        self.assertEqual(check_substring("world hello world", "world"), "string starts with the given substring")

    def test_edge_case_empty(self):
        self.assertEqual(check_substring("", "world"), "string doesnt start with the given substring")

    def test_edge_case_none(self):
        self.assertEqual(check_substring("hello", None), "entered string isnt a substring")

    def test_edge_case_non_string(self):
        with self.assertRaises(TypeError):
            check_substring(123, "world")

    def test_edge_case_non_string2(self):
        with self.assertRaises(TypeError):
            check_substring("hello", 123)

    def test_edge_case_non_string3(self):
        with self.assertRaises(TypeError):
            check_substring(None, "world")

    def test_edge_case_non_string4(self):
        with self.assertRaises(TypeError):
            check_substring("hello", None)
