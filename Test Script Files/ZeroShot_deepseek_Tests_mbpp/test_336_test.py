import unittest
from mbpp_336_code import check_monthnum

class TestCheckMonthnum(unittest.TestCase):

    def test_february(self):
        self.assertTrue(check_monthnum("February"))

    def test_other_months(self):
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
        self.assertFalse(check_monthnum(""))
        self.assertFalse(check_monthnum(None))
