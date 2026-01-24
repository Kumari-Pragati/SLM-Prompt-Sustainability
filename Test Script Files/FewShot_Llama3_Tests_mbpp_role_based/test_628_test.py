import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(replace_spaces("Hello World"), "0%20Hello%20World")

    def test_edge_case_max_length(self):
        self.assertEqual(replace_spaces("a" * 1000, ), "a" * 1000)

    def test_edge_case_max_length_exceeded(self):
        self.assertEqual(replace_spaces("a" * 1001), -1)

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_spaces(""), "")

    def test_edge_case_single_space(self):
        self.assertEqual(replace_spaces("a "), "a%0")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(replace_spaces("a b c"), "a%20b%20c")

    def test_edge_case_multiple_spaces_at_start(self):
        self.assertEqual(replace_spaces("   a b c"), "0%20%20a%20b%20c")

    def test_edge_case_multiple_spaces_at_end(self):
        self.assertEqual(replace_spaces("a b c   "), "a%20b%20c%20")
