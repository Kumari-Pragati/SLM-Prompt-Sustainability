import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSplchar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_splchar("Hello, World!"), "Hello World")
        self.assertEqual(remove_splchar("123_456_789"), "123456789")
        self.assertEqual(remove_splchar("_123_456_789_"), "123456789")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_splchar(""), "")

    def test_edge_case_single_char(self):
        self.assertEqual(remove_splchar("a"), "a")

    def test_edge_case_single_digit(self):
        self.assertEqual(remove_splchar("1"), "1")

    def test_edge_case_single_special_char(self):
        self.assertEqual(remove_splchar("!"), "")

    def test_edge_case_single_underscore(self):
        self.assertEqual(remove_splchar("_"), "")

    def test_edge_case_single_whitespace(self):
        self.assertEqual(remove_splchar(" "), "")

    def test_edge_case_single_digit_with_special_char(self):
        self.assertEqual(remove_splchar("1!"), "1")

    def test_edge_case_single_underscore_with_special_char(self):
        self.assertEqual(remove_splchar("_!"), "")

    def test_edge_case_single_whitespace_with_special_char(self):
        self.assertEqual(remove_splchar(" !"), "")

    def test_corner_case_multiple_special_chars(self):
        self.assertEqual(remove_splchar("!!!_____"), "")

    def test_corner_case_multiple_underscores(self):
        self.assertEqual(remove_splchar("_______"), "")
