import unittest
from mbpp_910_code import check_date

class TestCheckDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(check_date(12, 31, 2022))

    def test_leap_year(self):
        self.assertTrue(check_date(2, 29, 2024))

    def test_invalid_month(self):
        self.assertFalse(check_date(13, 31, 2022))

    def test_invalid_day(self):
        self.assertFalse(check_date(12, 32, 2022))

    def test_invalid_year(self):
        self.assertFalse(check_date(12, 31, 2020))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_date('a', 'b', 'c')
