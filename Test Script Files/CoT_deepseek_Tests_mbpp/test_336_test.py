import unittest
from mbpp_336_code import check_monthnum

class TestCheckMonthnum(unittest.TestCase):

    def test_february(self):
        self.assertTrue(check_monthnum("February"))

    def test_other_months(self):
        self.assertFalse(check_monthnum("January"))
        self.assertFalse(check_monthnum("March"))
        self.assertFalse(check_monthnum("April"))
        # Add more tests for other months as needed

    def test_empty_string(self):
        self.assertFalse(check_monthnum(""))

    def test_none(self):
        with self.assertRaises(TypeError):
            check_monthnum(None)

    def test_integer(self):
        with self.assertRaises(TypeError):
            check_monthnum(12)
