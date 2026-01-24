import unittest
from mbpp_762_code import check_monthnumber_number

class TestCheckMonthNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_monthnumber_number(4))
        self.assertTrue(check_monthnumber_number(6))
        self.assertTrue(check_monthnumber_number(9))
        self.assertTrue(check_monthnumber_number(11))

    def test_edge_cases(self):
        self.assertFalse(check_monthnumber_number(0))
        self.assertFalse(check_monthnumber_number(13))
        self.assertFalse(check_monthnumber_number(-1))

    def test_boundary_cases(self):
        self.assertTrue(check_monthnumber_number(3))
        self.assertTrue(check_monthnumber_number(5))
        self.assertTrue(check_monthnumber_number(7))
        self.assertTrue(check_monthnumber_number(8))
        self.assertTrue(check_monthnumber_number(10))
        self.assertTrue(check_monthnumber_number(12))
