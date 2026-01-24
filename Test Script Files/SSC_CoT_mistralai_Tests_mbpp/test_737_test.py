import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):

    def test_valid_string(self):
        self.assertEqual(check_str("A"), "Valid")
        self.assertEqual(check_str("Io"), "Valid")
        self.assertEqual(check_str("A1B2C3"), "Valid")
        self.assertEqual(check_str("_A1B2C3"), "Valid")
        self.assertEqual(check_str("A1B2C3_"), "Valid")

    def test_edge_cases(self):
        self.assertEqual(check_str("A "), "Invalid")
        self.assertEqual(check_str("A_"), "Invalid")
        self.assertEqual(check_str("1A"), "Invalid")
        self.assertEqual(check_str("A1"), "Invalid")
        self.assertEqual(check_str("A1B"), "Valid")
        self.assertEqual(check_str("A1B_"), "Valid")
        self.assertEqual(check_str("A_1B"), "Invalid")
        self.assertEqual(check_str("A_1B_"), "Invalid")

    def test_invalid_inputs(self):
        self.assertEqual(check_str(123), "Invalid")
        self.assertEqual(check_str(None), "Invalid")
        self.assertEqual(check_str(""), "Invalid")
        self.assertEqual(check_str(" "), "Invalid")
        self.assertEqual(check_str("!"), "Invalid")
        self.assertEqual(check_str("@"), "Invalid")
        self.assertEqual(check_str("#"), "Invalid")
        self.assertEqual(check_str("%"), "Invalid")
        self.assertEqual(check_str("^"), "Invalid")
        self.assertEqual(check_str("&"), "Invalid")
        self.assertEqual(check_str("*"), "Invalid")
        self.assertEqual(check_str("("), "Invalid")
        self.assertEqual(check_str(")"), "Invalid")
        self.assertEqual(check_str("_"), "Invalid")
