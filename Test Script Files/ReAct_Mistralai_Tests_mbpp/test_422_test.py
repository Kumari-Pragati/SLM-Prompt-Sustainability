import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):

    def test_positive_integer(self):
        """Test that the function correctly calculates the average of the cubes of positive integers"""
        self.assertAlmostEqual(find_Average_Of_Cube(3), 2.1666667, delta=0.000001)
        self.assertAlmostEqual(find_Average_Of_Cube(5), 6.04375, delta=0.000001)
        self.assertAlmostEqual(find_Average_Of_Cube(10), 158.730355, delta=0.000001)

    def test_zero(self):
        """Test that the function correctly handles the case of zero"""
        self.assertEqual(find_Average_Of_Cube(0), 0)

    def test_negative_integer(self):
        """Test that the function correctly handles negative integers"""
        self.assertAlmostEqual(find_Average_Of_Cube(-3), -2.1666667, delta=0.000001)
        self.assertRaises(ValueError, find_Average_Of_Cube, -1)

    def test_large_integer(self):
        """Test that the function correctly handles large integers"""
        self.assertAlmostEqual(find_Average_Of_Cube(1000), 12373378.182886, delta=0.000001)
