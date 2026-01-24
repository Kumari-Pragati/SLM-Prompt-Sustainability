import unittest
from mbpp_762_code import check_monthnumber_number

class TestCheckMonthNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_monthnumber_number(4))
        self.assertTrue(check_monthnumber_number(6))
        self.assertTrue(check_monthnumber_number(9))
        self.assertTrue(check_monthnumber_number(11))

    def test_edge_conditions(self):
        self.assertFalse(check_monthnumber_number(0))
        self.assertFalse(check_monthnumber_number(13))

    def test_boundary_conditions(self):
        self.assertTrue(check_monthnumber_number(1))
        self.assertTrue(check_monthnumber_number(3))
        self.assertTrue(check_monthnumber_number(5))
        self.assertTrue(check_monthnumber_number(7))
        self.assertTrue(check_monthnumber_number(8))
        self.assertTrue(check_monthnumber_number(10))
        self.assertTrue(check_monthnumber_number(12))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_monthnumber_number('4')
        with self.assertRaises(TypeError):
            check_monthnumber_number(None)
