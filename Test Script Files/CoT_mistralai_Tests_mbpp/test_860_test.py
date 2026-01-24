import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):
    def test_accept_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric("Hello123"), "Accept")
        self.assertEqual(check_alphanumeric("1234567890"), "Accept")
        self.assertEqual(check_alphanumeric("AbCdEfGhIjKlMnOpQrStUvWxYz"), "Accept")

    def test_reject_non_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric("Hello"), "Discard")
        self.assertEqual(check_alphanumeric("!@#$%^&*()_+-="), "Discard")
        self.assertEqual(check_alphanumeric("_"), "Discard")
        self.assertEqual(check_alphanumeric(" "), "Discard")
        self.assertEqual(check_alphanumeric("HelloWorld"), "Discard")
        self.assertEqual(check_alphanumeric("1234567890Hello"), "Discard")
        self.assertEqual(check_alphanumeric("Hello1234567890"), "Discard")

    def test_empty_string(self):
        self.assertEqual(check_alphanumeric(""), "Discard")

    def test_single_character(self):
        for char in range(ord('a'), ord('z') + 1):
            self.assertEqual(check_alphanumeric(chr(char)), "Discard")
        for char in range(ord('A'), ord('Z') + 1):
            self.assertEqual(check_alphanumeric(chr(char)), "Discard")
        for char in range(ord('0'), ord('9') + 1):
            self.assertEqual(check_alphanumeric(chr(char)), "Accept")
