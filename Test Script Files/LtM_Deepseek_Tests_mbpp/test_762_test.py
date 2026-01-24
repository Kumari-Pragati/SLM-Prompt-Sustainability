import unittest
from mbpp_762_code import check_monthnumber_number

class TestCheckMonthNumber(unittest.TestCase):

    def test_simple_valid_inputs(self):
        self.assertTrue(check_monthnumber_number(4))
        self.assertTrue(check_monthnumber_number(6))
        self.assertTrue(check_monthnumber_number(9))
        self.assertTrue(check_monthnumber_number(11))

    def test_edge_conditions(self):
        self.assertFalse(check_monthnumber_number(0))
        self.assertFalse(check_monthnumber_number(13))
        self.assertFalse(check_monthnumber_number(-1))

    def test_complex_cases(self):
        self.assertFalse(check_monthnumber_number(2))
        self.assertFalse(check_monthnumber_number(12))
        self.assertFalse(check_monthnumber_number(5))
        self.assertFalse(check_monthnumber_number(10))
