import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertTrue(check_Validity(3, 4, 5))
        self.assertTrue(check_Validity(4, 5, 6))
        self.assertTrue(check_Validity(5, 6, 7))

    def test_invalid_triangle(self):
        self.assertFalse(check_Validity(3, 3, 3))
        self.assertFalse(check_Validity(3, 4, 4))
        self.assertFalse(check_Validity(4, 3, 4))
        self.assertFalse(check_Validity(3, 5, 2))
        self.assertFalse(check_Validity(4, 6, 1))
        self.assertFalse(check_Validity(5, 7, 0))
