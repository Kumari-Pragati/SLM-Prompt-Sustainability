import unittest
from mbpp_910_code import datetime
from ninety_one_code import check_date

class TestCheckDate(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(check_date(2, 28, 2020))
        self.assertTrue(check_date(12, 31, 2021))
        self.assertTrue(check_date(2, 29, 2020))  # Leap year

    def test_invalid_date_format(self):
        self.assertFalse(check_date('a', 1, 2020))
        self.assertFalse(check_date(2, 'a', 2020))
        self.assertFalse(check_date(2, 28, 'a'))

    def test_invalid_month(self):
        self.assertFalse(check_date(13, 1, 2020))
        self.assertFalse(check_date(0, 1, 2020))
        self.assertFalse(check_date(12, 32, 2020))

    def test_invalid_day(self):
        self.assertFalse(check_date(2, 32, 2020))
        self.assertFalse(check_date(2, 0, 2020))
        self.assertFalse(check_date(2, -1, 2020))

    def test_invalid_year(self):
        self.assertFalse(check_date(0, 1, 2020))
        self.assertFalse(check_date(2, 28, 0))
        self.assertFalse(check_date(2, 28, 'a'))
