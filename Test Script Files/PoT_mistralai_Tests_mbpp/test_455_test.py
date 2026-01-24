import unittest
from mbpp_455_code import check_monthnumb_number

class TestCheckMonthnumbNumber(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(check_monthnumb_number(1))
        self.assertTrue(check_monthnumb_number(3))
        self.assertTrue(check_monthnumb_number(5))
        self.assertTrue(check_monthnumb_number(7))
        self.assertTrue(check_monthnumb_number(8))
        self.assertTrue(check_monthnumb_number(10))
        self.assertTrue(check_monthnumb_number(12))

    def test_edge_and_boundary_cases(self):
        self.assertFalse(check_monthnumb_number(0))
        self.assertFalse(check_monthnumb_number(13))
        self.assertFalse(check_monthnumb_number(2))
        self.assertFalse(check_monthnumb_number(4))
        self.assertFalse(check_monthnumb_number(6))
        self.assertFalse(check_monthnumb_number(9))
        self.assertFalse(check_monthnumb_number(11))
        self.assertFalse(check_monthnumb_number(-1))
        self.assertFalse(check_monthnumb_number(13.5))
        self.assertFalse(check_monthnumb_number('January'))
