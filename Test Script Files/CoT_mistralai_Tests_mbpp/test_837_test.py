import unittest
from mbpp_837_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(cube_Sum(1), 1)
        self.assertEqual(cube_Sum(2), 8)
        self.assertEqual(cube_Sum(3), 33)
        self.assertEqual(cube_Sum(4), 80)
        self.assertEqual(cube_Sum(5), 145)

    def test_zero(self):
        self.assertEqual(cube_Sum(0), 0)

    def test_negative_integer(self):
        self.assertRaises(ValueError, cube_Sum, -1)

    def test_floating_point(self):
        self.assertRaises(TypeError, cube_Sum, 2.5)

    def test_string(self):
        self.assertRaises(TypeError, cube_Sum, "test")
