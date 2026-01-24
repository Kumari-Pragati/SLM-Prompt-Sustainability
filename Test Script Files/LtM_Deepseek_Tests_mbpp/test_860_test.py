import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(check_alphanumeric("abc123"), "Accept")
        self.assertEqual(check_alphanumeric("ABC123"), "Accept")
        self.assertEqual(check_alphanumeric("123"), "Accept")

    def test_edge_conditions(self):
        self.assertEqual(check_alphanumeric(""), "Discard")
        self.assertEqual(check_alphanumeric(" "), "Discard")
        self.assertEqual(check_alphanumeric("@#$"), "Discard")

    def test_complex_cases(self):
        self.assertEqual(check_alphanumeric("abc123@#$"), "Discard")
        self.assertEqual(check_alphanumeric("123@#$"), "Discard")
        self.assertEqual(check_alphanumeric("abc@#$"), "Discard")
        self.assertEqual(check_alphanumeric("ABC"), "Accept")
        self.assertEqual(check_alphanumeric("123"), "Accept")
        self.assertEqual(check_alphanumeric("abc"), "Accept")
