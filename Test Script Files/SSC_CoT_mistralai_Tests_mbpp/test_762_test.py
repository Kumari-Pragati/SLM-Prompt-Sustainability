import unittest
from mbpp_762_code import check_monthnumber_number

class TestCheckMonthNumber(unittest.TestCase):
    def test_normal_input(self):
        self.assertTrue(check_monthnumber_number(4))
        self.assertTrue(check_monthnumber_number(6))
        self.assertTrue(check_monthnumber_number(9))
        self.assertTrue(check_monthnumber_number(11))

    def test_edge_input(self):
        self.assertFalse(check_monthnumber_number(0))
        self.assertFalse(check_monthnumber_number(1))
        self.assertFalse(check_monthnumber_number(2))
        self.assertFalse(check_monthnumber_number(3))
        self.assertFalse(check_monthnumber_number(12))
        self.assertFalse(check_monthnumber_number(13))
        self.assertFalse(check_monthnumber_number(14))
        self.assertFalse(check_monthnumber_number(15))

    def test_invalid_input(self):
        self.assertRaises(ValueError, check_monthnumber_number, -1)
        self.assertRaises(ValueError, check_monthnumber_number, float('inf'))
        self.assertRaises(ValueError, check_monthnumber_number, float('nan'))
        self.assertRaises(ValueError, check_monthnumber_number, 'a')
