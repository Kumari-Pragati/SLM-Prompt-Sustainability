import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(split_upperstring("AaaBbCc"), ["A", "Bb", "C"])
        self.assertListEqual(split_upperstring("A Aa Bb Cc"), ["A", "Aa", "Bb", "C"])
        self.assertListEqual(split_upperstring("A Aa Bb Cc Dd Ee"), ["A", "Aa", "Bb", "Cc", "Dd", "Ee"])

    def test_edge_case_empty_string(self):
        self.assertListEqual(split_upperstring(""), [])

    def test_edge_case_single_uppercase_letter(self):
        self.assertListEqual(split_upperstring("A"), ["A"])

    def test_edge_case_single_lowercase_letter(self):
        self.assertListEqual(split_upperstring("a"), [])

    def test_edge_case_all_uppercase_letters(self):
        self.assertListEqual(split_upperstring("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), ["A", "BC", "DE", "FG", "HI", "JK", "LM", "NO", "PQ", "RST", "UV", "WX", "YZ"])

    def test_edge_case_all_lowercase_letters(self):
        self.assertListEqual(split_upperstring("abcdefghijklmnopqrstuvwxyz"), [])

    def test_edge_case_mixed_uppercase_and_lowercase_letters(self):
        self.assertListEqual(split_upperstring("AbCdEfGhIjKlMnOpQrStUvWxYz"), ["A", "bC", "dE", "fG", "hI", "jK", "lM", "nOp", "qR", "sT", "uV", "wX", "yZ"])

    def test_edge_case_leading_and_trailing_whitespace(self):
        self.assertListEqual(split_upperstring("   AaaBbCc   "), ["A", "Bb", "C"])

    def test_edge_case_multiple_spaces(self):
        self.assertListEqual(split_upperstring("A   Aa   Bb   Cc"), ["A", "Aa", "Bb", "C"])

    def test_edge_case_non_alphabetic_characters(self):
        self.assertListEqual(split_upperstring("A1B2C3"), ["A", "B2", "C"])
        self.assertListEqual(split_upperstring("A_B_C_"), ["A", "B", "C"])
