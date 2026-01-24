import unittest
from mbpp_910_code import check_date

class TestCheckDate(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(check_date(1, 1, 2000))
        self.assertTrue(check_date(12, 31, 2020))
        self.assertTrue(check_date(9, 30, 2021))

    def test_invalid_date(self):
        self.assertFalse(check_date(13, 1, 2000))
        self.assertFalse(check_date(0, 1, 2000))
        self.assertFalse(check_date(1, 0, 2000))
        self.assertFalse(check_date(1, 31, 2000))
        self.assertFalse(check_date(1, 30, 1800))
        self.assertFalse(check_date(1, 30, 2100))

    def test_invalid_input(self):
        self.assertFalse(check_date('a', 1, 2000))
        self.assertFalse(check_date(1, 'b', 2000))
        self.assertFalse(check_date(1, 1, 'c'))
        self.assertFalse(check_date(1, 1, 2000.0))
        self.assertFalse(check_date(1, 1, None))
