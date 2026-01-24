import unittest
from mbpp_336_code import check_monthnum

class TestCheckMonthnum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertTrue(check_monthnum("February"))
        self.assertFalse(check_monthnum("January"))
        self.assertFalse(check_monthnum("March"))

    def test_edge_cases(self):
        self.assertFalse(check_monthnum(""))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_monthnum(123)
