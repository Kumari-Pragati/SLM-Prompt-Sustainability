import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):
    def test_accept_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric("abc123"), "Accept")
        self.assertEqual(check_alphanumeric("ABC123"), "Accept")
        self.assertEqual(check_alphanumeric("_123abc"), "Accept")

    def test_reject_non_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric("abc!"), "Discard")
        self.assertEqual(check_alphanumeric("ABC@"), "Discard")
        self.assertEqual(check_alphanumeric("_123!@"), "Discard")
        self.assertEqual(check_alphanumeric("123"), "Discard")
        self.assertEqual(check_alphanumeric("abc"), "Discard")

    def test_accept_empty_string(self):
        self.assertEqual(check_alphanumeric(""), "Accept")

    def test_accept_single_character_string(self):
        for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_':
            self.assertEqual(check_alphanumeric(char), "Accept")

    def test_reject_multi_non_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric("abc!@#$%^&*()"), "Discard")
