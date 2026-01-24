import unittest
from mbpp_336_code import check_monthnum

class TestCheckMonthnum(unittest.TestCase):
    def test_valid_month(self):
        self.assertTrue(check_monthnum("February"))

    def test_invalid_month(self):
        self.assertFalse(check_monthnum("January"))

    def test_invalid_month_type(self):
        with self.assertRaises(TypeError):
            check_monthnum(123)

    def test_invalid_month_case(self):
        self.assertFalse(check_monthnum("february"))

    def test_invalid_month_case2(self):
        self.assertFalse(check_monthnum("FEBRUARY"))

    def test_invalid_month_case3(self):
        self.assertFalse(check_monthnum("FEB"))

    def test_invalid_month_case4(self):
        self.assertFalse(check_monthnum("FEBR"))
