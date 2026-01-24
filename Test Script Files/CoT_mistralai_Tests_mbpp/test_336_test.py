import unittest
from mbpp_336_code import check_monthnum

class TestCheckMonthnum(unittest.TestCase):
    def test_february(self):
        self.assertTrue(check_monthnum("February"))

    def test_other_months(self):
        months = ["January", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        for month in months:
            self.assertFalse(check_monthnum(month))

    def test_invalid_input(self):
        self.assertFalse(check_monthnum("Invalid Month"))
        self.assertFalse(check_monthnum(12345))
        self.assertFalse(check_monthnum(None))
        self.assertFalse(check_monthnum(""))
