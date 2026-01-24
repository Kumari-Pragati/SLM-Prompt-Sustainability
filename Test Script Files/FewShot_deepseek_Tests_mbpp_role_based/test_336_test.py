import unittest
from mbpp_336_code import check_monthnum

class TestCheckMonthnum(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_monthnum("February"))

    def test_non_typical_case(self):
        self.assertFalse(check_monthnum("January"))

    def test_edge_case(self):
        self.assertTrue(check_monthnum("February"))

    def test_boundary_case(self):
        self.assertFalse(check_monthnum(""))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_monthnum(123)
