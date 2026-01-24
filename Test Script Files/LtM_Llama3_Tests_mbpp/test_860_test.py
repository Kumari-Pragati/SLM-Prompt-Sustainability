import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(check_alphanumeric("hello"), "Accept")

    def test_simple_invalid_input(self):
        self.assertEqual(check_alphanumeric("123"), "Discard")

    def test_edge_case_empty_input(self):
        self.assertEqual(check_alphanumeric(""), "Discard")

    def test_edge_case_single_character_input(self):
        self.assertEqual(check_alphanumeric("a"), "Accept")

    def test_edge_case_single_digit_input(self):
        self.assertEqual(check_alphanumeric("1"), "Accept")

    def test_edge_case_mixed_input(self):
        self.assertEqual(check_alphanumeric("hello123"), "Accept")

    def test_edge_case_non_alphanumeric_input(self):
        self.assertEqual(check_alphanumeric("!@#"), "Discard")

    def test_edge_case_non_alphanumeric_and_digit_input(self):
        self.assertEqual(check_alphanumeric("!@#123"), "Discard")

    def test_edge_case_non_alphanumeric_and_letter_input(self):
        self.assertEqual(check_alphanumeric("!@hello"), "Discard")

    def test_edge_case_non_alphanumeric_and_mixed_input(self):
        self.assertEqual(check_alphanumeric("!@#hello123"), "Discard")
