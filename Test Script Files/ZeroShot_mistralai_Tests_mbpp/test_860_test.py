import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(check_alphanumeric(""), "Discard")

    def test_all_alphabets(self):
        self.assertEqual(check_alphanumeric("abcdefghijklmnopqrstuvwxyz"), "Discard")

    def test_all_numbers(self):
        self.assertEqual(check_alphanumeric("1234567890"), "Accept")

    def test_mixed_alphanumeric(self):
        self.assertEqual(check_alphanumeric("abc123"), "Accept")

    def test_trailing_alphanumeric(self):
        self.assertEqual(check_alphanumeric("abc1234"), "Accept")

    def test_leading_alphanumeric(self):
        self.assertEqual(check_alphanumeric("123abc"), "Accept")

    def test_multiple_trailing_alphanumeric(self):
        self.assertEqual(check_alphanumeric("abc123456"), "Accept")

    def test_multiple_leading_alphanumeric(self):
        self.assertEqual(check_alphanumeric("123456abc"), "Accept")

    def test_only_special_characters(self):
        self.assertEqual(check_alphanumeric("!@#$%^&*()_+-="), "Discard")
