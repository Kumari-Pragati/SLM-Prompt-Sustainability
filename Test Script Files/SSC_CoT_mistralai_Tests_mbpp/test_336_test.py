import unittest
from mbpp_336_code import months
from 336_code import check_monthnum

class TestCheckMonthnum(unittest.TestCase):
    def test_normal_input(self):
        for month in months:
            if month != months.february:
                self.assertFalse(check_monthnum(month))

    def test_edge_cases(self):
        self.assertFalse(check_monthnum("January"))
        self.assertFalse(check_monthnum("March"))
        self.assertFalse(check_monthnum("April"))
        self.assertFalse(check_monthnum("May"))
        self.assertFalse(check_monthnum("June"))
        self.assertFalse(check_monthnum("July"))
        self.assertFalse(check_monthnum("August"))
        self.assertFalse(check_monthnum("November"))
        self.assertFalse(check_monthnum("December"))

    def test_february(self):
        self.assertTrue(check_monthnum("February"))

    def test_invalid_input(self):
        self.assertFalse(check_monthnum("InvalidMonth"))
        self.assertFalse(check_monthnum(""))
        self.assertFalse(check_monthnum(None))
        self.assertFalse(check_monthnum(1))
        self.assertFalse(check_monthnum(12.5))
