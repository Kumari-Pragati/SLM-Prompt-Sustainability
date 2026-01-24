import unittest
from mbpp_336_code import check_monthnum

class TestCheckMonthnum(unittest.TestCase):

    def test_simple_valid_input(self):
        self.assertTrue(check_monthnum("February"))

    def test_edge_case_empty_input(self):
        self.assertFalse(check_monthnum(""))

    def test_boundary_case_non_month_input(self):
        self.assertFalse(check_monthnum("January"))
        self.assertFalse(check_monthnum("March"))
        self.assertFalse(check_monthnum("December"))

    def test_complex_case_case_sensitivity(self):
        self.assertFalse(check_monthnum("february"))
        self.assertFalse(check_monthnum("FeBRUARY"))

    def test_invalid_input_type(self):
        self.assertFalse(check_monthnum(123))
        self.assertFalse(check_monthnum(["February"]))
