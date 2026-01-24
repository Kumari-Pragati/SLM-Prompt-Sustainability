import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_whitespaces("Hello World"), "HelloWorld")

    def test_edge_case_leading_trailing_spaces(self):
        self.assertEqual(remove_whitespaces("   Hello World   "), "HelloWorld")

    def test_edge_case_only_spaces(self):
        self.assertEqual(remove_whitespaces("   "), "")

    def test_edge_case_mixed_case(self):
        self.assertEqual(remove_whitespaces("HeLlO wOrLd"), "HeLlOwOrLd")

    def test_edge_case_tab(self):
        self.assertEqual(remove_whitespaces("\tHello World"), "HelloWorld")

    def test_edge_case_newline(self):
        self.assertEqual(remove_whitespaces("\nHello World\n"), "HelloWorld")

    def test_corner_case_empty_string(self):
        self.assertEqual(remove_whitespaces(""), "")
