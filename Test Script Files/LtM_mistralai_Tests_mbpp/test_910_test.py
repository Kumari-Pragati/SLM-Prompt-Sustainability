import unittest
from mbpp_910_code import date
from910_code import check_date

class TestCheckDate(unittest.TestCase):
    def test_simple_valid_date(self):
        self.assertTrue(check_date(1, 1, 2000))
        self.assertTrue(check_date(12, 31, 2021))
        self.assertTrue(check_date(2, 29, 2020))

    def test_edge_cases(self):
        self.assertTrue(check_date(1, 1, 0))
        self.assertTrue(check_date(13, 1, 2021))
        self.assertTrue(check_date(2, 29, 1900))
        self.assertTrue(check_date(2, 29, 2022))

    def test_invalid_inputs(self):
        self.assertFalse(check_date('a', 1, 2021))
        self.assertFalse(check_date(1, 'b', 2021))
        self.assertFalse(check_date(1, 1, 'a'))
        self.assertFalse(check_date(None, 1, 2021))
        self.assertFalse(check_date(1, None, 2021))
        self.assertFalse(check_date(1, 1, None))
