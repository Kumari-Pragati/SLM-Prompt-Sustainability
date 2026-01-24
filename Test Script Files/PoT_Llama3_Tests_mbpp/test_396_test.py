import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):
    def test_typical_valid(self):
        self.assertEqual(check_char("a"), "Valid")

    def test_typical_invalid(self):
        self.assertEqual(check_char("A"), "Invalid")

    def test_edge_single_char(self):
        self.assertEqual(check_char("a"), "Valid")

    def test_edge_multiple_chars(self):
        self.assertEqual(check_char("aa"), "Invalid")

    def test_edge_single_char_with_space(self):
        self.assertEqual(check_char(" a"), "Invalid")

    def test_edge_multiple_chars_with_space(self):
        self.assertEqual(check_char(" a a"), "Invalid")

    def test_edge_single_char_with_punctuation(self):
        self.assertEqual(check_char("a!"), "Invalid")

    def test_edge_multiple_chars_with_punctuation(self):
        self.assertEqual(check_char("a!a"), "Invalid")

    def test_edge_single_char_with_digit(self):
        self.assertEqual(check_char("a1"), "Invalid")

    def test_edge_multiple_chars_with_digit(self):
        self.assertEqual(check_char("a1a"), "Invalid")

    def test_edge_single_char_with_special_char(self):
        self.assertEqual(check_char("a@"), "Invalid")

    def test_edge_multiple_chars_with_special_char(self):
        self.assertEqual(check_char("a@a"), "Invalid")
