import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_integer("123456"))
        self.assertTrue(check_integer("+123456"))
        self.assertTrue(check_integer("-123456"))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(check_integer("0"))
        self.assertTrue(check_integer("+0"))
        self.assertTrue(check_integer("-0"))
        self.assertFalse(check_integer(""))
        self.assertFalse(check_integer(" "))
        self.assertFalse(check_integer("+ "))
        self.assertFalse(check_integer("- "))

    def test_invalid_or_exceptional_inputs(self):
        self.assertFalse(check_integer("123a456"))
        self.assertFalse(check_integer("+123a456"))
        self.assertFalse(check_integer("-123a456"))
        self.assertFalse(check_integer("123456a"))
        self.assertFalse(check_integer("+123456a"))
        self.assertFalse(check_integer("-123456a"))
