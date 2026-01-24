import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):

    def test_equilateral_triangle(self):
        """Test for equilateral triangle with equal sides"""
        self.assertTrue(check_equilateral(3, 3, 3))

    def test_non_equilateral_triangle(self):
        """Test for non-equilateral triangle with unequal sides"""
        self.assertFalse(check_equilateral(3, 4, 5))

    def test_zero_side(self):
        """Test for zero-length side"""
        self.assertFalse(check_equilateral(0, 0, 0))

    def test_negative_side(self):
        """Test for negative-length side"""
        self.assertFalse(check_equilateral(-1, -1, -1))

    def test_mixed_sides(self):
        """Test for mixed-length sides"""
        self.assertFalse(check_equilateral(3, 4, 5))
        self.assertFalse(check_equilateral(5, 3, 4))
        self.assertFalse(check_equilateral(4, 5, 3))
