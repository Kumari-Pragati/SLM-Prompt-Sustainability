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
        self.assertEqual(cube_Sum(-1), -1)
        self.assertEqual(cube_Sum(-2), 512)
        self.assertEqual(cube_Sum(-3), 2431)
        self.assertEqual(cube_Sum(-4), 5376)
        self.assertEqual(cube_Sum(-5), 8857)
