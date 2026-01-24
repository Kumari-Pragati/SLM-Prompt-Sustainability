import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):
    def test_typical_input(self):
        self.assertTrue(check_integer("123456789"))
        self.assertTrue(check_integer("-123456789"))
        self.assertTrue(check_integer("+123456789"))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(check_integer("0"))
        self.assertTrue(check_integer("9"))
        self.assertTrue(check_integer("1234567890"))
        self.assertTrue(check_integer("-1234567890"))
        self.assertTrue(check_integer("+1234567890"))
        self.assertIsNone(check_integer(""))
        self.assertIsNone(check_integer("12345678901"))

    def test_special_cases(self):
        self.assertTrue(check_integer("+0"))
        self.assertTrue(check_integer("-0"))
        self.assertFalse(check_integer("1a"))
        self.assertFalse(check_integer("1e"))
        self.assertFalse(check_integer("1E"))
        self.assertFalse(check_integer("1_"))
        self.assertFalse(check_integer("1-"))
