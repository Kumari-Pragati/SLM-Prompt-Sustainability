import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_Validity(1, 2, 3))
        self.assertTrue(check_Validity(5, 12, 13))
        self.assertTrue(check_Validity(7, 24, 25))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(check_Validity(0, 1, 1))
        self.assertFalse(check_Validity(1, 0, 1))
        self.assertFalse(check_Validity(1, 1, 0))
        self.assertFalse(check_Validity(0, 0, 0))
        self.assertFalse(check_Validity(1, 1, 2))
        self.assertFalse(check_Validity(1, 2, 1))
        self.assertFalse(check_Validity(2, 1, 1))

    def test_corner_cases(self):
        self.assertFalse(check_Validity(1, 1, 1))
        self.assertFalse(check_Validity(1, 2, 2))
        self.assertFalse(check_Validity(2, 2, 1))
        self.assertFalse(check_Validity(2, 1, 2))
