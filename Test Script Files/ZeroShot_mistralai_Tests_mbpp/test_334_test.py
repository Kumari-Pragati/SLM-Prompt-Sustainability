import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertTrue(check_Validity(3, 4, 5))
        self.assertTrue(check_Validity(6, 8, 10))
        self.assertTrue(check_Validity(9, 12, 15))

    def test_invalid_triangle(self):
        self.assertFalse(check_Validity(3, 3, 3))
        self.assertFalse(check_Validity(3, 4, 2))
        self.assertFalse(check_Validity(4, 3, 3))
