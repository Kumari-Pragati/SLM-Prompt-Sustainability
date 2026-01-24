import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):

    def test_valid_single_lowercase_char(self):
        self.assertEqual(check_char("a"), "Valid")

    def test_valid_multi_lowercase_char_with_repeated_char(self):
        self.assertEqual(check_char("abab"), "Valid")

    def test_valid_multi_lowercase_char_with_different_chars(self):
        self.assertEqual(check_char("abcdefg"), "Valid")

    def test_edge_case_single_uppercase_char(self):
        self.assertEqual(check_char("A"), "Invalid")

    def test_edge_case_multi_uppercase_char(self):
        self.assertEqual(check_char("AB"), "Invalid")

    def test_edge_case_multi_digit_char(self):
        self.assertEqual(check_char("123"), "Invalid")

    def test_edge_case_multi_special_char(self):
        self.assertEqual(check_char("!@#$%^&*()_+-="), "Invalid")

    def test_edge_case_multi_special_and_digit_char(self):
        self.assertEqual(check_char("1!@#$%^&*()_+-="), "Invalid")

    def test_edge_case_multi_special_and_uppercase_char(self):
        self.assertEqual(check_char("A!@#$%^&*()_+-="), "Invalid")

    def test_edge_case_multi_special_and_lowercase_char(self):
        self.assertEqual(check_char("a!@#$%^&*()_+-="), "Invalid")

    def test_edge_case_multi_uppercase_and_digit_char(self):
        self.assertEqual(check_char("AB123"), "Invalid")

    def test_edge_case_multi_uppercase_and_special_char(self):
        self.assertEqual(check_char("AB!@#$%^&*()_+-="), "Invalid")

    def test_edge_case_multi_digit_and_special_char(self):
        self.assertEqual(check_char("1!@#$%^&*()_+-="), "Invalid")
