import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):
    def test_simple_alphanumeric(self):
        self.assertEqual(check_alphanumeric("abc123"), "Accept")
        self.assertEqual(check_alphanumeric("ABC123"), "Accept")
        self.assertEqual(check_alphanumeric("123abc"), "Accept")

    def test_edge_cases(self):
        self.assertEqual(check_alphanumeric("abc123_"), "Accept")
        self.assertEqual(check_alphanumeric("abc123."), "Accept")
        self.assertEqual(check_alphanumeric("abc123_."), "Discard")
        self.assertEqual(check_alphanumeric("abc123_123"), "Discard")
        self.assertEqual(check_alphanumeric("abc123_123."), "Discard")

    def test_complex_cases(self):
        self.assertEqual(check_alphanumeric("abc123_ABC123"), "Accept")
        self.assertEqual(check_alphanumeric("123abc_ABC123"), "Accept")
        self.assertEqual(check_alphanumeric("abc123_ABC123_"), "Discard")
        self.assertEqual(check_alphanumeric("abc123_ABC123_123"), "Discard")
        self.assertEqual(check_alphanumeric("abc123_ABC123_123."), "Discard")
