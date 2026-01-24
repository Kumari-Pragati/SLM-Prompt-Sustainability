import unittest
from mbpp_336_code import check_monthnum

class TestCheckMonthnum(unittest.TestCase):
    def test_simple_february(self):
        self.assertTrue(check_monthnum("February"))

    def test_simple_other_months(self):
        self.assertFalse(check_monthnum("January"))
        self.assertFalse(check_monthnum("March"))
        self.assertFalse(check_monthnum("April"))
        self.assertFalse(check_monthnum("May"))
        self.assertFalse(check_monthnum("June"))
        self.assertFalse(check_monthnum("July"))
        self.assertFalse(check_monthnum("August"))
        self.assertFalse(check_monthnum("September"))
        self.assertFalse(check_monthnum("October"))
        self.assertFalse(check_monthnum("November"))
        self.assertFalse(check_monthnum("December"))

    def test_edge_case_month_names(self):
        self.assertFalse(check_monthnum("Januar"))
        self.assertFalse(check_monthnum("März"))
        self.assertFalse(check_monthnum("Apríl"))
        self.assertFalse(check_monthnum("Mai"))
        self.assertFalse(check_monthnum("Juni"))
        self.assertFalse(check_monthnum("Juli"))
        self.assertFalse(check_monthnum("Augustus"))
        self.assertFalse(check_monthnum("Septemberus"))
        self.assertFalse(check_monthnum("Octobers"))
        self.assertFalse(check_monthnum("Novembers"))
        self.assertFalse(check_monthnum("Decembers"))

    def test_invalid_input(self):
        self.assertFalse(check_monthnum(""))
        self.assertFalse(check_monthnum(123))
        self.assertFalse(check_monthnum(True))
        self.assertFalse(check_monthnum(None))
