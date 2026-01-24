import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):

    def test_typical_integer(self):
        self.assertTrue(check_integer("123"))

    def test_typical_negative_integer(self):
        self.assertTrue(check_integer("-123"))

    def test_typical_positive_integer(self):
        self.assertTrue(check_integer("+123"))

    def test_typical_integer_with_leading_zero(self):
        self.assertTrue(check_integer("0123"))

    def test_edge_case_empty_string(self):
        self.assertIsNone(check_integer(""))

    def test_edge_case_single_character(self):
        self.assertFalse(check_integer("a"))

    def test_edge_case_single_digit(self):
        self.assertTrue(check_integer("1"))

    def test_edge_case_single_plus(self):
        self.assertTrue(check_integer("+"))

    def test_edge_case_single_minus(self):
        self.assertTrue(check_integer("-"))

    def test_edge_case_multiple_characters(self):
        self.assertFalse(check_integer("abc"))

    def test_edge_case_multiple_digits(self):
        self.assertTrue(check_integer("12345"))

    def test_edge_case_multiple_digits_with_leading_zero(self):
        self.assertTrue(check_integer("012345"))

    def test_edge_case_multiple_digits_with_leading_plus(self):
        self.assertTrue(check_integer("+12345"))

    def test_edge_case_multiple_digits_with_leading_minus(self):
        self.assertTrue(check_integer("-12345"))

    def test_edge_case_multiple_characters_with_leading_plus(self):
        self.assertFalse(check_integer("+abc"))

    def test_edge_case_multiple_characters_with_leading_minus(self):
        self.assertFalse(check_integer("-abc"))

    def test_edge_case_multiple_digits_with_leading_plus_and_trailing_zero(self):
        self.assertTrue(check_integer("+12300"))

    def test_edge_case_multiple_digits_with_leading_minus_and_trailing_zero(self):
        self.assertTrue(check_integer("-12300"))

    def test_edge_case_multiple_digits_with_leading_plus_and_trailing_zero_and_leading_zero(self):
        self.assertTrue(check_integer("+012300"))

    def test_edge_case_multiple_digits_with_leading_minus_and_trailing_zero_and_leading_zero(self):
        self.assertTrue(check_integer("-012300"))

    def test_invalid_input_non_integer(self):
        self.assertFalse(check_integer("abc123"))

    def test_invalid_input_non_integer_with_leading_plus(self):
        self.assertFalse(check_integer("+abc123"))

    def test_invalid_input_non_integer_with_leading_minus(self):
        self.assertFalse(check_integer("-abc123"))

    def test_invalid_input_non_integer_with_leading_plus_and_trailing_zero(self):
        self.assertFalse(check_integer("+abc12300"))

    def test_invalid_input_non_integer_with_leading_minus_and_trailing_zero(self):
        self.assertFalse(check_integer("-abc12300"))
