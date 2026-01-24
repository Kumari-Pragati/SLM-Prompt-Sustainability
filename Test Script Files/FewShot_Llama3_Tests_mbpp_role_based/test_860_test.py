import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):
    def test_acceptable_string(self):
        self.assertEqual(check_alphanumeric("hello123"), "Accept")

    def test_unacceptable_string(self):
        self.assertEqual(check_alphanumeric("hello world"), "Discard")

    def test_empty_string(self):
        self.assertEqual(check_alphanumeric(""), "Discard")

    def test_single_character(self):
        self.assertEqual(check_alphanumeric("a"), "Accept")

    def test_single_digit(self):
        self.assertEqual(check_alphanumeric("1"), "Accept")

    def test_mixed_string(self):
        self.assertEqual(check_alphanumeric("hello123world"), "Accept")

    def test_non_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric("hello world!"), "Discard")
