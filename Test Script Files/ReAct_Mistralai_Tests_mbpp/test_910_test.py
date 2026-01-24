import unittest
from mbpp_910_code import check_date

class TestCheckDate(unittest.TestCase):

    def test_valid_date(self):
        # Typical case: valid date (month, day, year within valid range)
        self.assertTrue(check_date(1, 1, 2000))
        self.assertTrue(check_date(12, 31, 2022))
        self.assertTrue(check_date(2, 29, 2020))  # Leap year

    def test_invalid_date_month(self):
        # Edge case: invalid month (out of range)
        self.assertFalse(check_date(13, 1, 2000))
        self.assertFalse(check_date(0, 1, 2000))

    def test_invalid_date_day(self):
        # Edge case: invalid day (out of range for given month)
        self.assertFalse(check_date(2, 32, 2000))
        self.assertFalse(check_date(1, 32, 2000))
        self.assertFalse(check_date(2, 29, 2019))  # Not a leap year

    def test_invalid_date_year(self):
        # Edge case: invalid year (out of range)
        self.assertFalse(check_date(1, 1, 0))
        self.assertFalse(check_date(1, 1, 2100))  # Not a valid year

    def test_invalid_input_type(self):
        # Error case: invalid input type (non-integer for month, day, year)
        self.assertFalse(check_date('m', 1, 2000))
        self.assertFalse(check_date(1, 'd', 2000))
        self.assertFalse(check_date(1, 1, 'y'))
