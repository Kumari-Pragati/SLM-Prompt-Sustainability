import unittest
from mbpp_336_code import check_monthnum

class TestCheckMonthnum(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_monthnum("February"))

    def test_edge_case(self):
        self.assertFalse(check_monthnum("January"))
        self.assertFalse(check_monthnum("March"))

    def test_boundary_case(self):
        self.assertFalse(check_monthnum(""))
        self.assertFalse(check_monthnum(" " * 20))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_monthnum(123)
        with self.assertRaises(TypeError):
            check_monthnum(None)
