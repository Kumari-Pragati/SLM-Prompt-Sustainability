import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):
    def test_simple_valid(self):
        self.assertEqual(check_str("a"), "Valid")

    def test_simple_invalid(self):
        self.assertEqual(check_str("123"), "Invalid")

    def test_edge_empty(self):
        self.assertEqual(check_str(""), "Invalid")

    def test_edge_single_char(self):
        self.assertEqual(check_str("a"), "Valid")

    def test_edge_non_alphanumeric(self):
        self.assertEqual(check_str("_"), "Invalid")

    def test_edge_mixed_case(self):
        self.assertEqual(check_str("A"), "Valid")

    def test_edge_multiple_chars(self):
        self.assertEqual(check_str("abc"), "Valid")

    def test_edge_non_alphanumeric_chars(self):
        self.assertEqual(check_str("abc_"), "Valid")

    def test_edge_mixed_case_and_non_alphanumeric_chars(self):
        self.assertEqual(check_str("Abc_"), "Valid")
