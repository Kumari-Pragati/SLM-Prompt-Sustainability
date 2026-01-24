import unittest
from mbpp_336_code import check_monthnum

class TestCheckMonthnum(unittest.TestCase):

    def test_february(self):
        self.assertTrue(check_monthnum("February"))

    def test_january(self):
        self.assertFalse(check_monthnum("January"))

    def test_march(self):
        self.assertFalse(check_monthnum("March"))

    def test_april(self):
        self.assertFalse(check_monthnum("April"))

    def test_may(self):
        self.assertFalse(check_monthnum("May"))

    def test_june(self):
        self.assertFalse(check_monthnum("June"))

    def test_july(self):
        self.assertFalse(check_monthnum("July"))

    def test_august(self):
        self.assertFalse(check_monthnum("August"))

    def test_september(self):
        self.assertFalse(check_monthnum("September"))

    def test_october(self):
        self.assertFalse(check_monthnum("October"))

    def test_november(self):
        self.assertFalse(check_monthnum("November"))

    def test_december(self):
        self.assertFalse(check_monthnum("December"))

    def test_invalid_month(self):
        self.assertFalse(check_monthnum("Invalid Month"))
