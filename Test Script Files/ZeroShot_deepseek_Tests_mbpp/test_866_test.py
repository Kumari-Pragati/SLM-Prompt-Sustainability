import unittest
from mbpp_866_code import check_monthnumb

class TestCheckMonthNumb(unittest.TestCase):

    def test_valid_month(self):
        self.assertTrue(check_monthnumb("January"))
        self.assertTrue(check_monthnumb("March"))
        self.assertTrue(check_monthnumb("May"))
        self.assertTrue(check_monthnumb("July"))
        self.assertTrue(check_monthnumb("August"))
        self.assertTrue(check_monthnumb("October"))
        self.assertTrue(check_monthnumb("December"))

    def test_invalid_month(self):
        self.assertFalse(check_monthnumb("February"))
        self.assertFalse(check_monthnumb("April"))
        self.assertFalse(check_monthnumb("June"))
        self.assertFalse(check_monthnumb("September"))
        self.assertFalse(check_monthnumb("November"))
        self.assertFalse(check_monthnumb(""))
        self.assertFalse(check_monthnumb(None))
