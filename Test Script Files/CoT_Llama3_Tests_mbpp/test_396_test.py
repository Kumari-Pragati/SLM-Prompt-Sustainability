import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(check_char("a"), "Valid")
        self.assertEqual(check_char("abc"), "Valid")
        self.assertEqual(check_char("a"), "Valid")

    def test_invalid_input(self):
        self.assertEqual(check_char("A"), "Invalid")
        self.assertEqual(check_char("123"), "Invalid")
        self.assertEqual(check_char("abc123"), "Invalid")

    def test_edge_cases(self):
        self.assertEqual(check_char(""), "Invalid")
        self.assertEqual(check_char("a"), "Valid")
        self.assertEqual(check_char("a"), "Valid")

    def test_repeated_chars(self):
        self.assertEqual(check_char("aa"), "Valid")
        self.assertEqual(check_char("abcabc"), "Valid")
