import unittest
from mbpp_910_code import datetime
from910_code import check_date

class TestCheckDate(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(check_date(1, 1, 2022))
        self.assertTrue(check_date(2, 29, 2020))
        self.assertTrue(check_date(12, 31, 2021))

    def test_invalid_date_month(self):
        self.assertFalse(check_date(13, 1, 2022))
        self.assertFalse(check_date(0, 1, 2022))

    def test_invalid_date_day(self):
        self.assertFalse(check_date(1, 32, 2022))
        self.assertFalse(check_date(1, 0, 2022))

    def test_invalid_date_year(self):
        self.assertFalse(check_date(1, 1, 0))
        self.assertFalse(check_date(1, 1, 2023))
        self.assertFalse(check_date(1, 1, -1))

    def test_invalid_input(self):
        self.assertFalse(check_date('a', 1, 2022))
        self.assertFalse(check_date(1, 'b', 2022))
        self.assertFalse(check_date(1, 1, 'a'))
