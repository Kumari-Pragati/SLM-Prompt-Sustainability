import unittest
from mbpp_820_code import check_monthnum_number

class TestCheckMonthnumNumber(unittest.TestCase):
    def test_valid_months(self):
        self.assertTrue(check_monthnum_number(2))
        self.assertFalse(check_monthnum_number(1))
        self.assertFalse(check_monthnum_number(3))
        self.assertFalse(check_monthnum_number(4))
        self.assertFalse(check_monthnum_number(5))
        self.assertFalse(check_monthnum_number(6))
        self.assertFalse(check_monthnum_number(7))
        self.assertFalse(check_monthnum_number(8))
        self.assertFalse(check_monthnum_number(9))
        self.assertFalse(check_monthnum_number(10))
        self.assertFalse(check_monthnum_number(11))
        self.assertFalse(check_monthnum_number(12))

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, check_monthnum_number, 0)
        self.assertRaises(ValueError, check_monthnum_number, -1)
        self.assertRaises(ValueError, check_monthnum_number, 13)
        self.assertRaises(ValueError, check_monthnum_number, float('nan'))
        self.assertRaises(ValueError, check_monthnum_number, 'str')
