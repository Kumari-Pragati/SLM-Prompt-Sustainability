import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertTrue(check_Validity(3, 4, 5))
        self.assertTrue(check_Validity(6, 8, 10))
        self.assertTrue(check_Validity(4, 6, 7))

    def test_invalid_triangle(self):
        self.assertFalse(check_Validity(3, 3, 3))
        self.assertFalse(check_Validity(0, 0, 0))
        self.assertFalse(check_Validity(1, 2, 3))
        self.assertFalse(check_Validity(-1, 2, 3))
        self.assertFalse(check_Validity(1, -2, 3))
        self.assertFalse(check_Validity(1, 2, -3))

    def test_edge_cases(self):
        self.assertTrue(check_Validity(0, 0, 1))
        self.assertTrue(check_Validity(1, 0, 0))
        self.assertTrue(check_Validity(0, 1, 0))
