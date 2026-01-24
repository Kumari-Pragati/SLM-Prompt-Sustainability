import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):
    def test_accept_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric("abc123"), "Accept")

    def test_accept_empty_string(self):
        self.assertEqual(check_alphanumeric(""), "Accept")

    def test_accept_single_alphabet(self):
        self.assertEqual(check_alphanumeric("a"), "Accept")

    def test_accept_single_numeric(self):
        self.assertEqual(check_alphanumeric("1"), "Accept")

    def test_accept_mixed_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric("ab1c2d3"), "Accept")

    def test_reject_non_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric("@#$%^&*()"), "Discard")

    def test_reject_alphabet_only_string(self):
        self.assertEqual(check_alphanumeric("abcdefghijklmnopqrstuvwxyz"), "Discard")

    def test_reject_numeric_only_string(self):
        self.assertEqual(check_alphanumeric("1234567890"), "Discard")
