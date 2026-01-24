import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(replace_spaces("Hello World"), "0 2 % 0 1 2 0 2 % 0 1 2 0 1 2 0 2 % 0 1 2 0 1 2 0 1 2 0 2 %"), "Typical input test passed.")

    def test_edge_case_max_length(self):
        self.assertEqual(replace_spaces("a"*1000), "a"*1000, "Edge case max length test passed.")

    def test_edge_case_max_length_exceeded(self):
        self.assertEqual(replace_spaces("a"*1001), -1, "Edge case max length exceeded test passed.")

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_spaces(""), "", "Edge case empty string test passed.")

    def test_edge_case_single_space(self):
        self.assertEqual(replace_spaces("a"), "a", "Edge case single space test passed.")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(replace_spaces("a b c"), "0 2 % 0 1 2 0 2 % 0 1 2 0 1 2 0 2 %", "Edge case multiple spaces test passed.")

    def test_edge_case_multiple_spaces_max_length(self):
        self.assertEqual(replace_spaces("a b c"*1000), "a b c"*1000, "Edge case multiple spaces max length test passed.")

    def test_edge_case_multiple_spaces_max_length_exceeded(self):
        self.assertEqual(replace_spaces("a b c"*1001), -1, "Edge case multiple spaces max length exceeded test passed.")
