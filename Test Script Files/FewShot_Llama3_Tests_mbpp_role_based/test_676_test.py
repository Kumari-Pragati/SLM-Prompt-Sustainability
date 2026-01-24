import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_extra_char("Hello, World!"), "HelloWorld")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_extra_char(""), "")

    def test_edge_case_single_char(self):
        self.assertEqual(remove_extra_char("a"), "a")

    def test_edge_case_multiple_chars(self):
        self.assertEqual(remove_extra_char("abc"), "abc")

    def test_edge_case_non_alphanumeric_chars(self):
        self.assertEqual(remove_extra_char("Hello, World!"), "HelloWorld")

    def test_edge_case_multiple_non_alphanumeric_chars(self):
        self.assertEqual(remove_extra_char("Hello, World!@#"), "HelloWorld")

    def test_edge_case_mixed_chars(self):
        self.assertEqual(remove_extra_char("Hello, World!abc123"), "HelloWorldabc123")

    def test_edge_case_spaces(self):
        self.assertEqual(remove_extra_char("Hello World"), "HelloWorld")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(remove_extra_char("Hello   World"), "HelloWorld")

    def test_edge_case_tabs(self):
        self.assertEqual(remove_extra_char("Hello\tWorld"), "HelloWorld")

    def test_edge_case_newlines(self):
        self.assertEqual(remove_extra_char("Hello\nWorld"), "HelloWorld")
