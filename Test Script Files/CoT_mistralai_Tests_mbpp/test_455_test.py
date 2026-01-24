import unittest
from mbpp_455_code import check_monthnumb_number

class TestCheckMonthnumbNumber(unittest.TestCase):
    def test_valid_months(self):
        self.assertTrue(check_monthnumb_number(1))
        self.assertTrue(check_monthnumb_number(3))
        self.assertTrue(check_monthnumb_number(5))
        self.assertTrue(check_monthnumb_number(7))
        self.assertTrue(check_monthnumb_number(8))
        self.assertTrue(check_monthnumb_number(10))
        self.assertTrue(check_monthnumb_number(12))

    def test_invalid_months(self):
        self.assertFalse(check_monthnumb_number(0))
        self.assertFalse(check_monthnumb_number(2))
        self.assertFalse(check_monthnumb_number(4))
        self.assertFalse(check_monthnumb_number(6))
        self.assertFalse(check_monthnumb_number(9))
        self.assertFalse(check_monthnumb_number(11))
        self.assertFalse(check_monthnumb_number(13))

    def test_non_integer_input(self):
        self.assertFalse(check_monthnumb_number('str'))
        self.assertFalse(check_monthnumb_number(3.14))
        self.assertFalse(check_monthnumb_number([1, 2, 3]))
