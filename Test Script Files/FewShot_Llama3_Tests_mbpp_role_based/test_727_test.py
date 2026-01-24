import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_char("Hello, World!"), "HelloWorld")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_char(""), "")

    def test_edge_case_single_char(self):
        self.assertEqual(remove_char("a"), "a")

    def test_edge_case_multiple_chars(self):
        self.assertEqual(remove_char("abc"), "abc")

    def test_edge_case_non_alphanumeric_chars(self):
        self.assertEqual(remove_char("Hello, World!"), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars(self):
        self.assertEqual(remove_char("Hello, World!@#"), "HelloWorld")

    def test_edge_case_mixed_chars(self):
        self.assertEqual(remove_char("Hello, World!abc123"), "HelloWorldabc123")
