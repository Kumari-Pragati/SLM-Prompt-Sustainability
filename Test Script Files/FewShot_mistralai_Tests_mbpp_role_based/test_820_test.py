import unittest
from mbpp_820_code import check_monthnum_number

class TestCheckMonthnumNumber(unittest.TestCase):
    def test_valid_month_2(self):
        self.assertTrue(check_monthnum_number(2))

    def test_invalid_month_1(self):
        self.assertFalse(check_monthnum_number(1))

    def test_invalid_month_3(self):
        self.assertFalse(check_monthnum_number(3))

    def test_invalid_month_13(self):
        self.assertFalse(check_monthnum_number(13))
