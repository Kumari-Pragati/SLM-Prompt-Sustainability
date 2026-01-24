import unittest
from mbpp_820_code import check_monthnum_number

class TestCheckMonthNumNumber(unittest.TestCase):

    def test_check_monthnum_number_with_2(self):
        self.assertTrue(check_monthnum_number(2))

    def test_check_monthnum_number_with_other_number(self):
        self.assertFalse(check_monthnum_number(1))
        self.assertFalse(check_monthnum_number(3))
        self.assertFalse(check_monthnum_number(0))
        self.assertFalse(check_monthnum_number(-1))
