import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):
    def test_acceptable_string(self):
        self.assertEqual(check_alphanumeric("hello123"), "Accept")

    def test_discardable_string(self):
        self.assertEqual(check_alphanumeric("hello world"), "Discard")

    def test_empty_string(self):
        self.assertEqual(check_alphanumeric(""), "Discard")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            check_alphanumeric(123)

    def test_mixed_case_string(self):
        self.assertEqual(check_alphanumeric("Hello123"), "Accept")

    def test_numeric_string(self):
        self.assertEqual(check_alphanumeric("123456"), "Accept")

    def test_alphabetic_string(self):
        self.assertEqual(check_alphanumeric("abcdefghijklmnopqrstuvwxyz"), "Accept")
