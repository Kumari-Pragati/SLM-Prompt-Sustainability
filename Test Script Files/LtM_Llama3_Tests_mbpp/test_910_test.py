import unittest
from mbpp_910_code import check_date

class TestCheckDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(check_date(1, 1, 2022))
    def test_valid_date_leap_year(self):
        self.assertTrue(check_date(2, 29, 2024))
    def test_invalid_date_month(self):
        self.assertFalse(check_date(13, 1, 2022))
    def test_invalid_date_day(self):
        self.assertFalse(check_date(1, 32, 2022))
    def test_invalid_date_year(self):
        self.assertFalse(check_date(1, 1, 2020))
    def test_invalid_date_all(self):
        self.assertFalse(check_date(13, 32, 2020))
