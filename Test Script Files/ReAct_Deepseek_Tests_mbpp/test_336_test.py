import unittest
from mbpp_336_code import check_monthnum

class TestCheckMonthnum(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_monthnum("February"))

    def test_non_typical_case(self):
        self.assertFalse(check_monthnum("January"))

    def test_edge_case_lowercase(self):
        self.assertTrue(check_monthnum("february"))

    def test_edge_case_capitalization(self):
        self.assertTrue(check_monthnum("FeBrAy"))

    def test_edge_case_extra_spaces(self):
        self.assertTrue(check_monthnum("  February  "))

    def test_error_case_invalid_input(self):
        with self.assertRaises(TypeError):
            check_monthnum(123)

    def test_error_case_none_input(self):
        with self.assertRaises(TypeError):
            check_monthnum(None)
