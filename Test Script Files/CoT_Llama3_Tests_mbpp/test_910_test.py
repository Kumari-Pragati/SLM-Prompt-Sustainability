import unittest
from mbpp_910_code import check_date

class TestCheckDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(check_date(1, 1, 2022))

    def test_invalid_month(self):
        self.assertFalse(check_date(13, 1, 2022))

    def test_invalid_day(self):
        self.assertFalse(check_date(1, 32, 2022))

    def test_invalid_year(self):
        self.assertFalse(check_date(1, 1, 2022))

    def test_leap_year(self):
        self.assertTrue(check_date(2, 29, 2024))

    def test_non_leap_year(self):
        self.assertFalse(check_date(2, 29, 2023))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_date('a', 1, 2022)

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            check_date(1, 1, '2022')
