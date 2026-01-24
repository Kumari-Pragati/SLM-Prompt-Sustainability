import unittest
from mbpp_762_code import check_monthnumber_number

class TestCheckMonthnumberNumber(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertTrue(check_monthnumber_number(4))
        self.assertTrue(check_monthnumber_number(6))
        self.assertTrue(check_monthnumber_number(9))
        self.assertTrue(check_monthnumber_number(11))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(check_monthnumber_number(0))
        self.assertFalse(check_monthnumber_number(1))
        self.assertFalse(check_monthnumber_number(2))
        self.assertFalse(check_monthnumber_number(3))
        self.assertFalse(check_monthnumber_number(12))
        self.assertFalse(check_monthnumber_number(13))
        self.assertFalse(check_monthnumber_number(-1))

    def test_complex_scenarios(self):
        self.assertFalse(check_monthnumber_number(14))
        self.assertFalse(check_monthnumber_number(15))
        self.assertFalse(check_monthnumber_number(30))
        self.assertFalse(check_monthnumber_number(31))
        self.assertFalse(check_monthnumber_number(32))
        self.assertFalse(check_monthnumber_number(33))
        self.assertFalse(check_monthnumber_number(34))
        self.assertFalse(check_monthnumber_number(35))
        self.assertFalse(check_monthnumber_number(36))
        self.assertFalse(check_monthnumber_number(37))
        self.assertFalse(check_monthnumber_number(38))
        self.assertFalse(check_monthnumber_number(39))
