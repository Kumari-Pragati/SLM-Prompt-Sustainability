import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(check_alphanumeric("abc123"), "Accept")
        self.assertEqual(check_alphanumeric("ABC123"), "Accept")
        self.assertEqual(check_alphanumeric("123"), "Accept")
        self.assertEqual(check_alphanumeric("abc"), "Accept")

    def test_edge_cases(self):
        self.assertEqual(check_alphanumeric(""), "Discard")
        self.assertEqual(check_alphanumeric(" "), "Discard")
        self.assertEqual(check_alphanumeric("!@#"), "Discard")
        self.assertEqual(check_alphanumeric("$%^"), "Discard")

    def test_explicitly_handled_error_cases(self):
        self.assertEqual(check_alphanumeric(None), "Discard")
        self.assertEqual(check_alphanumeric(123), "Discard")
        self.assertEqual(check_alphanumeric(["abc123"]), "Discard")
