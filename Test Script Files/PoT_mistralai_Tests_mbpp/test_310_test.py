import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(string_to_tuple("hello world"), ("hello", "world"))

    def test_edge_case_empty_string(self):
        self.assertEqual(string_to_tuple(""), ())

    def test_edge_case_single_char(self):
        self.assertEqual(string_to_tuple("a"), ("a",))

    def test_edge_case_single_space(self):
        self.assertEqual(string_to_tuple(" "), ())

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(string_to_tuple("   "), ())

    def test_corner_case_leading_trailing_spaces(self):
        self.assertEqual(string_to_tuple("  hello world  "), ("hello", "world"))

    def test_corner_case_only_spaces(self):
        self.assertEqual(string_to_tuple("   "), ())
