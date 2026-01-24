import unittest
from mbpp_820_code import check_monthnum_number

class TestCheckMonthnumNumber(unittest.TestCase):
    def test_valid_monthnum1(self):
        self.assertTrue(check_monthnum_number(2))

    def test_invalid_monthnum1(self):
        self.assertFalse(check_monthnum_number(1))
        self.assertFalse(check_monthnum_number(3))
        self.assertFalse(check_monthnum_number(4))
        self.assertFalse(check_monthnum_number(5))

    def test_edge_case_monthnum1(self):
        self.assertFalse(check_monthnum_number(0))
        self.assertFalse(check_monthnum_number(12))
