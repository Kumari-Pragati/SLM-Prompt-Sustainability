import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):

    def test_positive_numbers(self):
        """Test positive numbers in valid triangle"""
        self.assertTrue(check_Validity(3, 4, 5))
        self.assertTrue(check_Validity(4, 3, 5))
        self.assertTrue(check_Validity(4, 5, 3))

    def test_zero_or_negative_numbers(self):
        """Test zero or negative numbers in invalid triangle"""
        self.assertFalse(check_Validity(0, 0, 0))
        self.assertFalse(check_Validity(-1, 0, 0))
        self.assertFalse(check_Validity(0, -1, 0))
        self.assertFalse(check_Validity(0, 0, -1))
        self.assertFalse(check_Validity(-1, -1, 0))
        self.assertFalse(check_Validity(0, -1, -1))
        self.assertFalse(check_Validity(-1, 0, -1))

    def test_edge_cases(self):
        """Test edge cases of valid and invalid triangles"""
        self.assertTrue(check_Validity(1, 1, 2))
        self.assertTrue(check_Validity(2, 1, 1))
        self.assertFalse(check_Validity(1, 1, 1))
        self.assertFalse(check_Validity(0, 0, 1))
        self.assertFalse(check_Validity(1, 0, 0))
        self.assertFalse(check_Validity(0, 1, 0))
