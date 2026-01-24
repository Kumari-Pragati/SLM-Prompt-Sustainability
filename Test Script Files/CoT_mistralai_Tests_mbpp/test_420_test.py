import unittest
from mbpp_420_code import cube_Sum

class TestCubeSum(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(cube_Sum(1), 8)
        self.assertEqual(cube_Sum(2), 64)
        self.assertEqual(cube_Sum(3), 168)
        self.assertEqual(cube_Sum(10), 10240)

    def test_zero(self):
        self.assertEqual(cube_Sum(0), 0)

    def test_negative_integer(self):
        self.assertRaises(ValueError, cube_Sum, -1)

    def test_float(self):
        self.assertRaises(TypeError, cube_Sum, 3.14)

    def test_string(self):
        self.assertRaises(TypeError, cube_Sum, 'abc')
