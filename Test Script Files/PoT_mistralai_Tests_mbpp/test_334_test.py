import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(check_Validity(2, 1, 3))
        self.assertTrue(check_Validity(3, 2, 4))
        self.assertTrue(check_Validity(4, 3, 5))
        self.assertTrue(check_Validity(1, 3, 4))
        self.assertTrue(check_Validity(3, 4, 5))
        self.assertTrue(check_Validity(4, 5, 6))

    def test_edge_cases(self):
        self.assertTrue(check_Validity(0, 0, 1))
        self.assertTrue(check_Validity(1, 0, 0))
        self.assertTrue(check_Validity(0, 1, 0))
        self.assertTrue(check_Validity(1, 1, 2))
        self.assertTrue(check_Validity(2, 1, 1))
        self.assertTrue(check_Validity(1, 2, 1))

    def test_boundary_cases(self):
        self.assertTrue(check_Validity(1, 1, 2))
        self.assertTrue(check_Validity(2, 2, 3))
        self.assertTrue(check_Validity(3, 3, 4))

    def test_invalid_inputs(self):
        self.assertFalse(check_Validity(-1, 1, 2))
        self.assertFalse(check_Validity(1, -1, 2))
        self.assertFalse(check_Validity(1, 1, -1))
        self.assertFalse(check_Validity(None, 1, 2))
        self.assertFalse(check_Validity(1, None, 2))
        self.assertFalse(check_Validity(1, 2, None))
