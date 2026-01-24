import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):

    def test_accept_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric("abc123"), "Accept")
        self.assertEqual(check_alphanumeric("ABC123"), "Accept")
        self.assertEqual(check_alphanumeric("123abc"), "Accept")
        self.assertEqual(check_alphanumeric("_123abc"), "Accept")
        self.assertEqual(check_alphanumeric("ABC_123"), "Accept")

    def test_reject_non_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric("abc!"), "Discard")
        self.assertEqual(check_alphanumeric("ABC!"), "Discard")
        self.assertEqual(check_alphanumeric("123@"), "Discard")
        self.assertEqual(check_alphanumeric("_123@"), "Discard")
        self.assertEqual(check_alphanumeric("ABC_@"), "Discard")

    def test_empty_string(self):
        self.assertEqual(check_alphanumeric(""), "Discard")

    def test_single_character(self):
        for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_':
            self.assertEqual(check_alphanumeric(char), "Accept")
