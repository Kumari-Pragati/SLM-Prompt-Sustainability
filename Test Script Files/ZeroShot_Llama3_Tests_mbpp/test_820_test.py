import unittest
from mbpp_820_code import check_monthnum_number

class TestCheckMonthnumNumber(unittest.TestCase):

    def test_check_monthnum_number_true(self):
        self.assertTrue(check_monthnum_number(2))

    def test_check_monthnum_number_false(self):
        self.assertFalse(check_monthnum_number(1))

    def test_check_monthnum_number_false2(self):
        self.assertFalse(check_monthnum_number(13))

    def test_check_monthnum_number_false3(self):
        self.assertFalse(check_monthnum_number(0))

    def test_check_monthnum_number_false4(self):
        self.assertFalse(check_monthnum_number(-1))
