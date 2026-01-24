import unittest
from mbpp_910_code import datetime

def check_date(m, d, y):
    try:
        m, d, y = map(int, (m, d, y))
        datetime.date(y, m, d)
        return True
    except ValueError:
        return False

class TestCheckDate(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(check_date(1, 1, 2022))
        self.assertTrue(check_date(12, 31, 2022))
        self.assertTrue(check_date(2, 29, 2020))

    def test_invalid_date_month(self):
        self.assertFalse(check_date(13, 1, 2022))
        self.assertFalse(check_date(0, 1, 2022))

    def test_invalid_date_day(self):
        self.assertFalse(check_date(1, 32, 2022))
        self.assertFalse(check_date(1, 0, 2022))

    def test_invalid_date_year(self):
        self.assertFalse(check_date(1, 1, 2023))
        self.assertFalse(check_date(1, 1, 1900))
