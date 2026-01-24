import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(check_alphanumeric("abc123"), "Accept")
        self.assertEqual(check_alphanumeric("ABC123"), "Accept")
        self.assertEqual(check_alphanumeric("abc_123"), "Accept")
        self.assertEqual(check_alphanumeric("ABC_123"), "Accept")

    def test_edge_case(self):
        self.assertEqual(check_alphanumeric(""), "Discard")
        self.assertEqual(check_alphanumeric(" "), "Discard")
        self.assertEqual(check_alphanumeric("a"), "Discard")
        self.assertEqual(check_alphanumeric("A"), "Discard")
        self.assertEqual(check_alphanumeric("0"), "Discard")
        self.assertEqual(check_alphanumeric("9"), "Discard")
        self.assertEqual(check_alphanumeric("_"), "Discard")

    def test_boundary_case(self):
        self.assertEqual(check_alphanumeric("a0"), "Accept")
        self.assertEqual(check_alphanumeric("A0"), "Accept")
        self.assertEqual(check_alphanumeric("0a"), "Accept")
        self.assertEqual(check_alphanumeric("0A"), "Accept")
        self.assertEqual(check_alphanumeric("_a"), "Accept")
        self.assertEqual(check_alphanumeric("_A"), "Accept")
        self.assertEqual(check_alphanumeric("a_"), "Accept")
        self.assertEqual(check_alphanumeric("A_"), "Accept")
