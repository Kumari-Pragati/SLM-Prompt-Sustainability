import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertTrue(is_allowed_specific_char("hello"))
        self.assertTrue(is_allowed_specific_char("123"))
        self.assertTrue(is_allowed_specific_char("hello.123"))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(is_allowed_specific_char(""))
        self.assertTrue(is_allowed_specific_char("a")
        self.assertTrue(is_allowed_specific_char("0")
        self.assertTrue(is_allowed_specific_char(".")

    def test_invalid_inputs(self):
        self.assertFalse(is_allowed_specific_char("hello!"))
        self.assertFalse(is_allowed_specific_char("123!"))
        self.assertFalse(is_allowed_specific_char("hello.123!"))
