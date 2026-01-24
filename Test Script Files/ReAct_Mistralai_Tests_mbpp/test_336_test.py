import unittest
from mbpp_336_code import check_monthnum

class TestCheckMonthnum(unittest.TestCase):

    def test_february(self):
        self.assertTrue(check_monthnum("February"))

    def test_other_months(self):
        for month in ["January", "March", "April", "June", "July", "August", "October", "November", "December"]:
            self.assertFalse(check_monthnum(month))

    def test_invalid_input(self):
        self.assertFalse(check_monthnum("Invalid Month"))
        self.assertFalse(check_monthnum(None))
        self.assertFalse(check_monthnum(""))
        self.assertFalse(check_monthnum(123))
