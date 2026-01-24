import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_positive_integer(self):
        """Test cube_Sum function with positive integers"""
        self.assertEqual(cube_Sum(1), 1)
        self.assertEqual(cube_Sum(2), 8)
        self.assertEqual(cube_Sum(3), 33)
        self.assertEqual(cube_Sum(10), 2772)

    def test_zero(self):
        """Test cube_Sum function with zero"""
        self.assertEqual(cube_Sum(0), 0)

    def test_negative_integer(self):
        """Test cube_Sum function with negative integers"""
        self.assertEqual(cube_Sum(-1), -1)
        self.assertEqual(cube_Sum(-2), -64)
        self.assertEqual(cube_Sum(-3), -261)

    def test_large_integer(self):
        """Test cube_Sum function with large integers"""
        self.assertEqual(cube_Sum(1000), 64656000000000000000)
